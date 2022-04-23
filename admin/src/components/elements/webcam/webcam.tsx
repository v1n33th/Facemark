import { forwardRef, useImperativeHandle, useRef } from "react";
import ReactWebcam from "react-webcam";
type Props = {
  styleClassName: string;
};
function Webcam({ styleClassName }: any, ref: any) {
  const webcamRef: any = useRef();

  useImperativeHandle(ref, () => ({
    video: webcamRef?.current?.video,
    width: webcamRef?.current?.width,
    height: webcamRef?.current?.height,
  }));

  return (
    <ReactWebcam
      className={styleClassName}
      ref={webcamRef}
      muted={true}
      audio={false}
      screenshotFormat="image/jpeg"
    />
  );
}
export default forwardRef(Webcam);
