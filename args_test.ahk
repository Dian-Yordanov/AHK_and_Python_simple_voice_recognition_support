test_case := "press space"
; Check the number of arguments
if (A_Args.Length() = 0)
{
    MsgBox, No arguments were passed to the script.
}
else
{
    ; Loop through the arguments and display each one
    ;for index, arg in A_Args
    ;{
    ;    MsgBox, Argument %index%: %arg%
    ;}
    ; MsgBox, % A_Args[2]
    if (A_Args[2] = test_case)
    {
        MsgBox, "ok"
    }
}
