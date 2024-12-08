; Define the RunCMD function
RunCMD(command) {
    ; Open the command prompt, execute the command, and keep the window open
RunWait, cmd.exe /c nslookup myip.opendns.com resolver1.opendns.com | clip
}

; Example usage of the RunCMD function
RunCMD("echo Hello, World!")
