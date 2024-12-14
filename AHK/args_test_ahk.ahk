test_case := "press space"
arg_string := % A_Args[2]

if (A_Args.Length() = 0)
{
    MsgBox, No arguments were passed to the script.
}
else
{
    if (A_Args[2] = test_case)
    {
        MsgBox, "ok" + %arg_string%
    }
    else
    {
        MsgBox, "NOT ok" + %arg_string%
    }
}
