#!/usr/bin/perl
$|=1;
print "cpu speed test\n";
$^T=time();
$tsize=10000000;
while ($size < $tsize)
	{
	@array[$size++]=1;
	}
$diff=time()-$^T;
print "total time to count $tsize  $diff seconds\n";
