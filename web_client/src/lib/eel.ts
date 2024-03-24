eel.expose(toggleUIRunningState);
export function toggleUIRunningState() {
  const stopButton = document.querySelector(
    "#status-start #stop"
  ) as HTMLButtonElement;
  if (!stopButton) return;
  stopButton.click();
}

function setImage(id: string, base64: string) {
  const base64Prefix = "data:image/png;base64,";
  const img = document.getElementById(id) as HTMLImageElement;
  if (!img) return;
  img.src = base64Prefix + base64;
}

eel.expose(setEnemyImage);
export function setEnemyImage(base64: string) {
  setImage("status-feedback-enemy-image", base64);
}

eel.expose(setMapImage);
export function setMapImage(base64: string) {
  setImage("status-feedback-map-image", base64);
}
