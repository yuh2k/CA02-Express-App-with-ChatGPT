mkdir jan_photos
cd jan_photos
for i in {01..31}; do mkdir photos$i; done
for i in {01..31}; do touch photos$i/notes.txt; done
cd photos27
pwd
cd ../photos28
ls -la
cd ..
ls *1
ls -d *1*
rm -r jan_photos