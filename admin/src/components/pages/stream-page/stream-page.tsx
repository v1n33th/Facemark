import { useEffect, useRef, useState } from "react";
import { loadModels } from "../../../services/utils/face-utils";
import FaceDetect from "../../modules/face-detect/face-detect";
import styles from "./stream-page.module.css";

function StreamPage() {
  const [loading, setLoading] = useState(true);
  const [model, setModel] = useState<any>();
  const [error, setError] = useState("");

  useEffect(() => {
    setLoading(true);
    loadModels()
      .then((models) => {
        setModel(models);
      })
      .catch((err) => {
        console.log(err);
        setError(err);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }
  if (error) {
    return <div>{"Error occured"}</div>;
  }

  return (
    <div>
      <h1 className={styles["heading"]}>Face mark</h1>

      <FaceDetect model={model} />
    </div>
  );
}

export default StreamPage;
