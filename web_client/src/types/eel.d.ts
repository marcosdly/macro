type EelPromise<T> = Promise<(callback: (result: T) => Promise<void>) => void>;
// EelPromise<string> === await func().then((T) => T)


declare interface Eel {
  expose(f: Function): void;

}

declare const eel: Eel;
