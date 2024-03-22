import {
  Component,
  Context,
  RefObject,
  createContext,
  createRef,
  render,
} from "preact";
import { StateUpdater, useState } from "preact/hooks";

interface DropdownItemProps {
  title: string;
  index: number;
  indexRef: RefObject<HTMLInputElement>;
  titleRef: RefObject<HTMLInputElement>;
  setOption: StateUpdater<OBSOption> | undefined;
}

export class SelectVideoInput extends Component {
  ref: RefObject<HTMLUListElement>;
  indexRef: RefObject<HTMLInputElement>;
  titleRef: RefObject<HTMLInputElement>;
  setOption: StateUpdater<OBSOption> | undefined;
  VideoInputContext: Context<StateUpdater<OBSOption>>;

  constructor() {
    super();
    this.ref = createRef();
    this.indexRef = createRef();
    this.titleRef = createRef();
    this.VideoInputContext = createContext({} as StateUpdater<OBSOption>);
  }

  DropdownItem(props: DropdownItemProps) {
    const click = async (ev: MouseEvent) => {
      ev.preventDefault();
      if (!props.setOption) return;
      props.setOption(props);
      const eelCallback = await eel.setOBSInputOptions(
        props.title,
        props.index
      );
      eelCallback(async () => {
        props.indexRef.current!.value = props.index.toString();
        props.titleRef.current!.value = props.title;
      });
    };

    return (
      <li>
        <a className="dropdown-item" onClick={click}>
          {props.title}
        </a>
      </li>
    );
  }

  async refreshOptions(): Promise<void> {
    const eelCallback = await eel.getOBSInputOptions();

    eelCallback(async (result) => {
      const objs = JSON.parse(result) as OBSOption[];
      const components = objs.map((option) => (
        <>
          <this.DropdownItem
            title={option.title}
            index={option.index}
            setOption={this.setOption}
            indexRef={this.indexRef}
            titleRef={this.titleRef}
          />
        </>
      ));
      render(components, this.ref.current!);
    });
  }

  render() {
    const [option, setOption] = useState({} as OBSOption);
    this.setOption = setOption;

    return (
      <this.VideoInputContext.Provider value={setOption}>
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
            <ul className="dropdown-menu" ref={this.ref}></ul>
          </div>
          <input
            className="rounded bg-secondary-subtle border-0 text-bg-light p-1"
            type="text"
            name="video-input-index"
            id="video-input-index"
            ref={this.indexRef}
            disabled
            value={option.index}
            placeholder="-"
          />
          <input
            className="rounded bg-secondary-subtle border-0 text-bg-light p-1"
            type="text"
            name="video-input-name"
            id="video-input-name"
            ref={this.titleRef}
            disabled
            value={option.title}
            placeholder="-"
          />
          <button
            onClick={this.refreshOptions}
            type="button"
            className="btn btn-secondary rounded"
          >
            Reload
          </button>
        </div>
      </this.VideoInputContext.Provider>
    );
  }

  componentDidMount(): void {
    this.refreshOptions();
  }
}
