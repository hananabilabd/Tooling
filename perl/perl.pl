print "hello from perl\n";
$x=5;
print "x = $x\n";
@array = (1,2,3);
print "$array[2]\n";
print "@array\n";
%data = ('Ahmed','s','Rana',23);
print "data{'Ahmed'} = $data{'Ahmed'}\n";
if ($x ==5 ) {
print "true x = $x\n";

}
else {
print "	False x = $x\n";
}
if ( (2 <=> 5) == -1){ # if left hand side is less than right  it returns -1 
print "hello\n";
}
@arr=(1,2,3,4);
for ( $i=0 ; $i <3 ; $i=$i +1){
	print "array[$i]=$array[$i]\n";
}
open ( file , "<import.txt");
$line = <file> ;
chomp($line); #to remove the \n  from the read line 
print "$line";
$line = <file> ;
print "$line";
print "please enter your name " ;
$input = <STDIN>;
print " you entered $input ";
################################################## write in a file 
open ( file , ">>import.txt");
print file " hello in the file " ;
