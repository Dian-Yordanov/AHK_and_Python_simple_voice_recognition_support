test_case := "press space"
arg_string := % A_Args[2]
continue_boolean = False

; Function to check if either half of a sentence is present in a text
CheckHalfSentence(sentence, text) {
    ; Calculate the length of the sentence and divide it into halves
    half_length := StrLen(sentence) // 2
    first_half := SubStr(sentence, 1, half_length)
    second_half := SubStr(sentence, half_length + 1)

    ; Check if either half is present in the text
    first_half_present := InStr(text, first_half)
    second_half_present := InStr(text, second_half)

    return first_half_present || second_half_present
}

test_func(message, test_case) { 
    MsgBox, "++++++++" + %message%
}

check_if_phrase_is_whole_or_contained(test_case, func){
    global arg_string
    if (A_Args.Length() = 0)
        {
            MsgBox, "Condition is NOT met"
        }
    else
    {
        if (A_Args[2] = test_case)
        {
            continue_boolean = True
            MsgBox, "condition is met exactly" + %arg_string%
        }
        else
        {
            result := CheckHalfSentence(test_case, arg_string)
    
            if (result)
            {
                continue_boolean = True
                MsgBox, condition is PARTLY met + %arg_string%
            }
            else
            {
                MsgBox, Condition is NOT met + %arg_string%
            }
        }
    }

    if(continue_boolean){
        return %func%(arg_string, test_case) 
    }

}

check_if_phrase_is_whole_or_contained(test_case, "test_func")