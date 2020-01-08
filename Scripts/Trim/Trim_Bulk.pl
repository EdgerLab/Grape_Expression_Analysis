#!/usr/bin/env perl -w
use strict;
use warnings;
use Cwd;
# Reads my master pair file and sends each unit in that csv to be submitted
my $file = $ARGV[0] or die "Need to get CSV file on the command line\n"; 
open(my $data, '<', $file) or die "Could not open '$file' $!\n";
while (my $line = <$data>) {
	chomp $line;
	my @fields = split "," , $line;
	my $file1 = $fields[0];
	my $file2 = $fields[1];
	$file1 =~ s/\//\\\//g;
	$file2 =~ s/\//\\\//g;
	
	`cp submit_trim_files_BASE.sh Trim_Submit/submit_trim_files_$fields[2].sh`;
	chdir("/mnt/research/edgerpat_lab/Scotty/Grape_RNA_Seq/Scripts/Trim/Trim_Submit/") or die "Cannot change";
	`perl -pi -e "s/FILE1/$file1/g" submit_trim_files_$fields[2].sh`;
	`perl -pi -e "s/FILE2/$file2/g" submit_trim_files_$fields[2].sh`;
	`perl -pi -e "s/NAME/$fields[2]/g" submit_trim_files_$fields[2].sh`;
	`sbatch submit_trim_files_$fields[2].sh`;
	chdir("../") or die "Cannot change";
}

