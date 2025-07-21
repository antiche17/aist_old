# activate_and_run_loop.ps1

# Перейти в рабочую папку
cd C:\qa\AIST

# Разрешить выполнение скриптов в рамках текущей сессии
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Активировать виртуальное окружение
.\.venv1\Scripts\Activate.ps1

# Цикл ввода и исполнения команд
do {
    $command = Read-Host "`nВведите команду (например: pytest test_order.py) или 'q' для выхода"
    
    if ($command -ne "q") {
        Invoke-Expression $command
    }

} while ($command -ne "q")

Write-Host "`n🟢 Скрипт завершён."
