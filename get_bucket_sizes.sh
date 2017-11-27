rm tmp.txt
while IFS=$'\t' read -r -a myArray
do
 echo "${myArray[0]}"
 echo "${myArray[1]}"
 echo "${myArray[2]}"
 bucket_url="gs://${myArray[2]}"
 bucket_size=$(gsutil du -s $bucket_url | awk '{print $1;}' )
 echo $bucket_size >> tmp.txt
done < broad-firecloud-testing.tsv
