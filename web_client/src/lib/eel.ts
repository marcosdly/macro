eel.expose(toggleUIRunningState);
export function toggleUIRunningState() {
  const stopButton = document.querySelector(
    "#status-start #stop"
  ) as HTMLButtonElement;
  if (!stopButton) return;
  stopButton.click();
}
