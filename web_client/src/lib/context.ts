import { VNode, createContext } from "preact";
import { StateUpdater } from "preact/hooks";

export const MainContext = createContext({} as [VNode, StateUpdater<VNode>]);
