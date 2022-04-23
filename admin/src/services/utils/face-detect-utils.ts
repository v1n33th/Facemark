import { useEffect } from "react";
import { useRerender } from "./common-hooks";

export const detect = async (model: any, webcam: any, canvas: any) => {
  if (
    typeof webcam !== "undefined" &&
    webcam !== null &&
    webcam?.video?.readyState === 4
  ) {
    // Get video
    const video = webcam.video;

    // Make detections

    const prediction = await model.estimateFaces(video, false);
    return prediction;
  }
};

export function useAndSetCanvasWidthAndHeight(
  canvas: HTMLCanvasElement,
  webcam: any
) {
  const { reRender, getReRenderedVal } = useRerender();
  console.log("Rerendered");
  useEffect(() => {
    const videoWidth = webcam?.video?.videoWidth ?? 0;
    const videoHeight = webcam?.video?.videoHeight ?? 0;
    if (webcam && canvas && videoWidth > 0 && videoHeight > 0) {
      //Set video height and width
      webcam.video.width = videoWidth;
      webcam.video.height = videoHeight;

      //Set canvas height and width
      canvas.width = videoWidth;
      canvas.height = videoHeight;

      //Set canvas height and width
      webcam.width = videoWidth;
      webcam.height = videoHeight;
      console.log("Rerendered22");
      reRender();
    }
  }, [webcam?.video?.videoWidth ?? 0, webcam?.video?.videoHeight ?? 0]);
}

export function setWebcamAndCanvasDimens(
  canvas: HTMLCanvasElement,
  webcam: any
) {
  const videoWidth = webcam?.video?.videoWidth ?? 0;
  const videoHeight = webcam?.video?.videoHeight ?? 0;
  if (webcam && canvas && videoWidth > 0 && videoHeight > 0) {
    //Set video height and width
    webcam.video.width = videoWidth;
    webcam.video.height = videoHeight;

    //Set canvas height and width
    canvas.width = videoWidth;
    canvas.height = videoHeight;

    //Set canvas height and width
    webcam.width = videoWidth;
    webcam.height = videoHeight;
    console.log("Rerendered22");
    return true;
  }
  return false;
}
