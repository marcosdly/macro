type EelPromise<T> = Promise<(callback: (result: T) => Promise<void>) => void>;
// EelPromise<string> === await func().then((T) => T)

interface OBSOption {
  title: string;
  index: number;
}

declare interface Eel {
  expose(f: Function): void;

  // Exposed by Python, Javascript will use
  getOBSInputOptions(): EelPromise<string>;
  setOBSInputOptions(title: string, index: number): EelPromise<void>;
}

declare const eel: Eel;
