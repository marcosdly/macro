interface ImageProps {
  elemId: string;
  title: string;
}

export function Image({ elemId, title }: ImageProps) {
  return (
    <div className="feedback-image-container">
      <label htmlFor={elemId} className="text-white p-1">
        {title}
      </label>
      <div className="image-container rounded p-1">
        <img id={elemId} alt="feedback image" className="text-white" />
      </div>
    </div>
  );
}

export function Feedback() {
  return (
    <div id="status-feedback" className="container">
      <div className="row">
        <div className="col">
          <Image elemId="status-feedback-enemy-image" title="Enemy" />
        </div>
        <div className="col">
          <Image elemId="status-feedback-map-image" title="Minimap" />
        </div>
      </div>
    </div>
  );
}
