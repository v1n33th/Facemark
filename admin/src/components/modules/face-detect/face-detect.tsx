import { useCallback, useEffect, useRef } from "react";
import { drawPredictionsToCanvas } from "../../../services/utils/canvas-utils";
import { useInterval } from "../../../services/utils/common-hooks";
import {
  detect,
  setWebcamAndCanvasDimens,
  useAndSetCanvasWidthAndHeight,
} from "../../../services/utils/face-detect-utils";
import Webcam from "../../elements/webcam/webcam";
import styles from "./face-detect.module.css";

type Props = {
  model: any;
};

function FaceDetect({ model }: Props) {
  const webcamRef: any = useRef();
  const canvasRef: any = useRef();

  const onTimer = useCallback(() => {
    setWebcamAndCanvasDimens(canvasRef.current, webcamRef.current);
    detect(model, webcamRef.current, canvasRef.current)
      .then((predictions) => {
        drawPredictionsToCanvas(predictions, canvasRef.current);
      })
      .catch((err) => {
        console.log(err);
      });
  }, [model, webcamRef.current, canvasRef.current]);

  useInterval(onTimer, 100);

  return (
    <>
      <Webcam ref={webcamRef} styleClassName={styles["common-styles"]} />
      <canvas ref={canvasRef} className={styles["common-styles"]} />
    </>
  );
}

export default FaceDetect;
