import "pe"
import "math"

rule python_script_detect
{
    meta:
        description = "CITS2006 Yara File"
        author = "23135002"
    strings:
	   $python_shebang = {23 21 2f 75 73 72 2f 62 69 6e 2f 65 6e 76 20 70 79 74 68 6f 6e ??} //check for python and python3
       $python_main = "if __name__ == \"__main__\"" nocase // Check for classic main statement
       $python_function = /def\s+\w+\s*\([^)]*\):/ // Check for any example of a python function
	condition:
	   any of them
}

rule powershell_script_detect
{
    strings:
	   $ps_start = "Start-Process" nocase // Common in powershell scripts
       $ps_invoke = "Invoke-Expression" nocase // Common in powershell scripts
       $ps_scriptblock = "ScriptBlock" nocase // Common in powershell scripts
       $ps_function = /function\s+\w+\s*{/ // Powershell function
       $ps_params = /param\s*\(\s*\[/ // Powershell params inside function (can't do multiple lines xd)
	condition:
	   any of them
}

rule VBscript_detect
{
    strings:
        $vb_create = "CreateObject(" nocase
        $vb_execute = "Execute(" nocase
    condition:
        any of them
}

rule script_keyword_match
{
    strings:
        $script = "Script" nocase 
    condition:
        uint16(0) != 0x5A4D and any of them
}