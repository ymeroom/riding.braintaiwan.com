@echo off
chcp 65001 > nul
echo =======================================================
echo    2026 東京單車騎旅 19日主題曲 Suno AI 全資產下載工具
echo =======================================================
echo.
echo 請從瀏覽器 DevTools (F12) 複製 Suno Bearer Token / Session Token。
echo (若留空直接按 Enter，將嘗試抓取公開 CDN 之 MP3 / LRC / 封面)
echo.
set /p SUNO_TOKEN="請貼上 Suno Token: "
echo.
if "%SUNO_TOKEN%"=="" (
    python suno_asset_downloader.py
) else (
    python suno_asset_downloader.py --token "%SUNO_TOKEN%"
)
echo.
echo =======================================================
echo 下載與標籤寫入作業已完成！
echo 產出檔案位置：
echo • MP3 與 LRC 歌詞：d:\2026東京單車騎旅\music\
echo • 高音質 WAV 母帶：d:\2026東京單車騎旅\wav\
echo • Stems 分軌 WAV：d:\2026東京單車騎旅\stems\
echo • 單車播放器：d:\2026東京單車騎旅\cycling_player.html
echo =======================================================
pause
