#!/usr/bin/perl
print "Content-type: text/plain\n\n";
print `perl -v`;
print `perl -V`;
print `find \`perl -e 'print "@INC"'\` -name '*.pm' -print`;
