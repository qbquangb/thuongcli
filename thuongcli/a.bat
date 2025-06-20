color 0A

if exist "D:\Duan\20publish_pypi\thuongcli\my_assistant.py" (
    echo Chay file my_assistant.py.
    cd /d D:\Duan\20publish_pypi\thuongcli
    "C:\Users\Hii\AppData\Local\Programs\Python\Python310\python.exe" "my_assistant.py"
) else (
    echo Khong tim thay file my_assistant.py, khong chay.
)