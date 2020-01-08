

cd /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Input_Files/Seq/20190809_mRNASeq_PE150/
ls -d "$PWD/"*gz | grep R1 > R1.txt
ls -d "$PWD/"*gz | grep R2 > R2.txt
ls -d *gz | grep R1 > R3.txt # get name
paste -d "," R1.txt R2.txt R3.txt > File_List.csv


cd /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Input_Files/Seq/20190802_mRNASeq_PE150/
ls -d "$PWD/"*gz | grep R1 > R1.txt
ls -d "$PWD/"*gz | grep R2 > R2.txt
ls -d *gz | grep R1 > R3.txt # get name
paste -d "," R1.txt R2.txt R3.txt > File_List.csv


cd /mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Input_Files/Seq/20190724_mRNASeq_PE150/
ls -d "$PWD/"*gz | grep R1 > R1.txt
ls -d "$PWD/"*gz | grep R2 > R2.txt
ls -d *gz | grep R1 > R3.txt # get name
paste -d "," R1.txt R2.txt R3.txt > File_List.csv
