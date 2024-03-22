import { createRef } from "preact";
import { useState } from "preact/hooks";

function StartButtons() {
  const playRef = createRef(),
    stopRef = createRef();

  const PlayIcon = () => <i class="bi bi-play-fill"></i>;
  const PlaySpinner = () => <div className="spinner-border"></div>;

  const [icon, setIcon] = useState(<PlayIcon />);

  const playOnClick = async (ev: MouseEvent) => {
    ev.preventDefault();
    const playButton = playRef.current! as HTMLButtonElement;
    const stopButton = stopRef.current! as HTMLButtonElement;
    const eelCallback = await eel.setRunningState(true);
    eelCallback(async (ok) => {
      if (!ok) return;
      setIcon(<PlaySpinner />);
      playButton.disabled = true;
      stopButton.disabled = false;
    });
  };

  const stopOnClick = async (ev: MouseEvent) => {
    ev.preventDefault();
    const playButton = playRef.current! as HTMLButtonElement;
    const stopButton = stopRef.current! as HTMLButtonElement;
    const eelCallback = await eel.setRunningState(false);
    eelCallback(async (ok) => {
      if (!ok) return;
      setIcon(<PlayIcon />);
      stopButton.disabled = true;
      playButton.disabled = false;
    });
  };

  return (
    <>
      <button
        type="button"
        className="btn btn-primary"
        id="start"
        ref={playRef}
        onClick={playOnClick}
      >
        {icon}
      </button>
      <button
        type="button"
        className="btn btn-danger"
        disabled
        id="stop"
        ref={stopRef}
        onClick={stopOnClick}
      >
        <i class="bi bi-stop-fill"></i>
      </button>
    </>
  );
}

function Visualize() {
  const ref = createRef();

  const click = async (ev: MouseEvent) => {
    ev.preventDefault();
    const button = ref.current! as HTMLInputElement;
    const state = Boolean(button.checked);
    const eelCallback = await eel.setVisualizeState(state);
    eelCallback(async (ok) => {
      if (ok) button.checked = state;
      else button.checked = false;
    });
  };

  return (
    <div id="status-start-visualize" className="form-check form-switch">
      <input
        type="checkbox"
        id="btn-check-outlined"
        className="form-check-input"
        role="switch"
        autocomplete="off"
        ref={ref}
        onClick={click}
      />
      <label htmlFor="btn-check-outlined" className="form-check-label">
        Visualize
      </label>
    </div>
  );
}

export function Start() {
  return (
    <div id="status-start">
      <StartButtons />
      <Visualize />
    </div>
  );
}
