#!/usr/bin/perl

open(InFile, cpmresult) || die;
while ($line = <InFile>)
            {
		my @arrOfString=split(/ /,$line);
		if ($hash{ "$arrOfString[0]$arrOfString[1] $arrOfString[2]" } == NULL || $hash{ "$arrOfString[0]$arrOfString[1] $arrOfString[2]" } < $arrOfString[3]) { 
			$hash{ "$arrOfString[0]$arrOfString[1] $arrOfString[2]" } = $arrOfString[3]
		}
            }

while ( my ($key, $value) = each(%hash) ) {
         print "$key => $value";
    }

close (InFile);
