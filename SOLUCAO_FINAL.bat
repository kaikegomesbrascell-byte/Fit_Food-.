@echo off
title Maps Pro - Solução Final
color 0A

echo.
echo ========================================
echo   MAPS PRO - INICIANDO SISTEMA
echo ========================================
echo.

cd sigilopay-landing\backend

echo [1/2] Instalando dependencias (se necessario)...
call npm install --silent

echo.
echo [2/2] Iniciando servidor...
echo.
echo ========================================
echo   SISTEMA PRONTO!
echo ========================================
echo.
echo Acesse: http://localhost:3000
echo.
echo Pressione Ctrl+C para parar
echo.

start http://localhost:3000

npm run dev
