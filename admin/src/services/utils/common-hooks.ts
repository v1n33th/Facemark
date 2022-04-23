import { useCallback, useEffect, useState } from "react";

export function useInterval(callback: () => void, delay: number) {
  useEffect(() => {
    const intervalId = setInterval(callback, delay);
    return () => clearInterval(intervalId);
  }, [callback, delay]);
}

export function useRerender() {
  const [state, setState] = useState<any>();
  console.log("rrer");
  const changedState = useCallback(() => {
    return state;
  }, [state]);

  return {
    reRender: () => setState({}),
    getReRenderedVal: changedState,
  };
}
