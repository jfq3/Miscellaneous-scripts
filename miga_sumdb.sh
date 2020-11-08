#!/bin/bash

echo "test begin!"
#create a sqlite datbase named summary.db
DB_NAME=summary.db
DB_TABLE=summary
CSV_FILE=summary.csv
haai=0.0
aai=0.0
ani=0.0
#rm $DB_NAME

sqlite3 $DB_NAME << CREATE_DB

DROP TABLE IF EXISTS $DB_TABLE;
create table summary(name varchar(256) UNIQUE, closest varchar(256), haai float, aai float, ani float);

CREATE_DB

#loop all files in dir
for file in ./*;
do
  #get file name and splite it.
  fullname=$(basename "$file")
  echo $fullname
  filename=$(echo $fullname | cut -d . -f1)
#  echo "filename: " $filename
  fmname="${fullname%.*}"
  middlename=$(echo $fmname | cut -d . -f2)
#  echo "middlename: " $middlename
  extension="${fullname##*.}"
#  echo "extension: " $extension
  
  if [ $filename == "summary" ]
  then
      echo "this is summary db. quit."
      continue
  fi

  if [ "$extension" != "db" ] && [ "$extension" != "txt" ] 
  then
      echo "this is not for using. quit."
      continue
  fi  
#  insert the file into summary table, if exist then ignore this insert.
  sqlite3 summary.db << INSERT_FILE
  insert or ignore into summary (name) values ("$filename");
INSERT_FILE
  #
  if [ $extension == "db" ];
  then
      echo "it is db"
      #process for haai, aai, and ani table
      if [ $middlename == "haai"  ]
      then
	echo "process haai table"
	#get haai value and update to summary table.
	haai=$( sqlite3 $fullname << HAAI_GET
	select MAX(aai) from aai;
HAAI_GET
	)
        sqlite3 summary.db << HAAI_UPDATE
	update summary set haai = $haai where name = "$filename";
HAAI_UPDATE

      elif [ $middlename == "aai" ]
      then
	echo "process aai table"
        #get aai value and update to summary table.
        aai=$( sqlite3 $fullname << AAI_GET
        select MAX(aai) from aai;
AAI_GET
        )
        sqlite3 summary.db << AAI_UPDATE
        update summary set aai = $aai where name = "$filename";
AAI_UPDATE

      elif [ $middlename == "ani" ]
      then
	echo "process ani table"
        #get ani value and update to summary table.
        ani=$( sqlite3 $fullname << ANI_GET
        select MAX(ani) from ani;
ANI_GET
        )
        sqlite3 summary.db << ANI_UPDATE
        update summary set ani = $ani where name = "$filename";
ANI_UPDATE
      else
	echo "something wrong!!!"
        break
      fi
  
  elif [ $extension == "txt" ]
  then
      echo "it is txt"
      line=$(head -n 1 $fullname)
      echo $line
      closest=$(echo $line | cut -d " " -f3)
      echo $closest
      sqlite3 summary.db << ANI_CLOSEST
      update summary set closest = "$closest" where name = "$filename";
ANI_CLOSEST

  else
      echo "it is other"
  fi

   
done

#echo "i get fullname: ", $fullname
rm $CSV_FILE
sqlite3 summary.db << CREATE_CSV
.head on
.mode csv
.once ./summary.csv
select * from summary;
CREATE_CSV

echo "Job Completed, Please see the summary.db or summary.csv file to check the collected results."

