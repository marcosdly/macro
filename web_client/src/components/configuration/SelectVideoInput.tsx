interface DropdownItemProps {
  title: string;
}

function DropdownItem({ title }: DropdownItemProps) {
  return (
    <>
      <li>
        <a className="dropdonw-item">{title}</a>
      </li>
    </>
  );
}

export function SelectVideoInput() {
  return (
    <div id="configuration-select-video-input">
      <div className="dropdown">
        <button
          className="btn btn-secondary dropdown-toggle"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
        >
          Select OBS Video Input
        </button>
        <ul className="dropdown-menu"></ul>
      </div>
      <input
        className="rounded bg-secondary-subtle border-0 text-bg-light p-1"
        type="text"
        name="video-input"
        id="video-input"
        disabled
      />
    </div>
  );
}
