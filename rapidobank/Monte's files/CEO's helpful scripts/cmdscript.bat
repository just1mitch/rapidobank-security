:: Batch file that imports network related .dll files
:: Generated by GitHub Copilot
@echo off
echo Loading netapi32.dll...
rundll32 netapi32.dll,ProcessIdleTasks
echo Done.

echo Pinging google.com...
ping google.com

echo Displaying network configuration...
ipconfig

echo Done.