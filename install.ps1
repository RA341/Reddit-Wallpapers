$p = &{python -V}

Function Get-Folder($initialDirectory=""){
    [System.Reflection.Assembly]::LoadWithPartialName("System.windows.forms")|Out-Null

    $foldername = New-Object System.Windows.Forms.FolderBrowserDialog
    $foldername.Description = "Select a folder"
    $foldername.rootfolder = "MyComputer"
    $foldername.SelectedPath = $initialDirectory

    if($foldername.ShowDialog() -eq "OK")
    {
        $folder += $foldername.SelectedPath
    }
    return $folder
}


if($p -is [System.Management.Automation.ErrorRecord]){
    Write-Host "python not installed exiting"
    Exit-PSHostProcess
} else {

    # file paths
    $installPath = Get-Folder

    $dir = $installPath + "\reddit-image-downloader\"
    $script_path = $dir + "main.py"
    $req_path = $dir + "req.txt"
    $subreddit_path = $dir + "subreddits.txt"
    $util_dir = $dir + "modules\"
    $file_man = $util_dir + "file_manager.py"
    $red_auth = $util_dir + "reddit_auth.py"

    # links for all files
    $script_uri = 'https://raw.githubusercontent.com/RA341/py-wallpaper-downloader/main/main.py'
    $subreddit_uri = "https://raw.githubusercontent.com/RA341/py-wallpaper-downloader/main/subreddits.txt"
    $req_uri = 'https://raw.githubusercontent.com/RA341/py-wallpaper-downloader/main/requirments.txt'
    $file_man_uri = 'https://raw.githubusercontent.com/RA341/py-wallpaper-downloader/main/modules/file_manager.py'
    $red_auth_uri = 'https://raw.githubusercontent.com/RA341/py-wallpaper-downloader/main/modules/reddit_auth.py'

    python -c "import sys; print(sys.executable)"

    if (Test-Path $dir) {
        # Perform Delete file from folder operation
        Write-Host "Folder Exists"
        Write-Host "Skipping"
    } else{
        #PowerShell Create directory if not exists
        New-Item $dir -ItemType Directory
        New-Item $util_dir -ItemType Directory
        Write-Host "Folder Created successfully"
    }

    Write-Host "Downloading required files"

    Write-Host "Downloading main Script"
    Invoke-WebRequest -URI $script_uri -OutFile $script_path

    Write-Host "Downloading Requirments file"
    Invoke-WebRequest -URI $req_uri -OutFile $req_path

    Write-Host "Downloading subreddit file"
    Invoke-WebRequest -URI $subreddit_uri -OutFile $subreddit_path

    Write-Host "Downloading file manager.py"
    Invoke-WebRequest -URI $file_man_uri -OutFile $file_man

    Write-Host "Downloading reddit auth script"
    Invoke-WebRequest -URI $red_auth_uri -OutFile $red_auth

    Write-Host "All Files Sucessfully downloaded"

    Write-Host "Downloading dependecies"
    Write-Host "Please wait this may take some time...."

    pip --disable-pip-version-check install -r $req_path

    Write-Host "Downloaded dependecies"

    Write-Host "Creating settings file"
    Set-Location $dir
    python -c "import sys; from modules.file_manager import createFiles ; createFiles()"

    Write-Host "Cleaning up"
    Remove-Item $req_path

#    $clean = Read-Host "Y or N"
#    if ($clean -eq 'y' -or $clean -eq 'Y')
#    {
#        Remove-Item $dir
#    }

#    $finalpythonpath = "pythonw.exe"
#    $finalscriptpath = '"'+ $script_path+'"'
#
#    $CIMTriggerClass = Get-CimClass -ClassName MSFT_TaskEventTrigger -Namespace Root/Microsoft/Windows/TaskScheduler:MSFT_TaskEventTrigger
#    $trigger = New-CimInstance -CimClass $CIMTriggerClass -ClientOnly
#
#    $trigger.Enabled = $true
#
#    $trigger.Subscription = '<QueryList><Query Id="0" Path="System"><Select
#    Path="System">*[System[Provider[@Name=''Microsoft-Windows-FilterManager''] and
#    EventID=6]]</Select></Query></QueryList>'
#
#    $taskname = 'recoil-control'
#
#
#    $action = New-ScheduledTaskAction -Execute $pythonpath
#    $action = New-ScheduledTaskAction -Execute $finalpythonpath -Argument $finalscriptpath
#
#    Register-ScheduledTask -Trigger $trigger -Action $action -TaskName $taskname
#
    Write-Host "Feel free to delete this powershell script"
    Read-Host "Press any key to exit"
}
