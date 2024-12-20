arg_string := % A_Args[2]

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

launch_function_matching_whole_or_part_of_hotstring(test_case, func, use_consensus_boolean){
    global arg_string
    message = %arg_string%
    continue_boolean := False
    consensus_boolean := False
    result := CheckHalfSentence(test_case, message)    
    ; MsgBox, %result%
    if (A_Args.Length() == 0)
        {
            MsgBox, "Condition is NOT met"
        }
    else
    {
        if (A_Args[1] == "1" and message == test_case) {
            continue_boolean := True  
            consensus_boolean := True
            ; MsgBox, Condition is fully met and agreed upon
        } 
        else if (A_Args[1] == "1" and result) {        
            if not use_consensus_boolean {
                continue_boolean := True  
                ; MsgBox, Condition is agreed upon but partially met
            }
        } 
        else if (A_Args[1] == "1" and not result) {        
            MsgBox, Condition is agreed upon but NOT met
        } 
        else if (A_Args[1] == "0") {
            if (message == test_case or result) {
                if (result) {
                    if use_consensus_boolean {
                        MsgBox, Condition is fully met but not agreed upon
                    } 
                    else {
                        consensus_boolean := True
                        continue_boolean := True
                        ; MsgBox, Condition is partially met but agreed upon
                    }
                } 
            } 
            else {
                MsgBox, Condition is NOT met
            }
        } 
        else {
            MsgBox, Condition is NOT met
        }
    }

    if(use_consensus_boolean) {
        if(continue_boolean and consensus_boolean){
            return %func%(arg_string, test_case) 
        }
    }
    else {
        if(continue_boolean){
            return %func%(arg_string, test_case) 
        }
    }
}

test_func(message, test_case) { 
    MsgBox, "++++++++" + %message%
}

test_case := "press space"

launch_function_matching_whole_or_part_of_hotstring("press space", "test_func", false)
launch_function_matching_whole_or_part_of_hotstring(test_case, "test_func", true)