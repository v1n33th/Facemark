import * as faceapi from "face-api.js";
import { MODELS_URL } from "../contants/path-contants";

export async function loadModels() {
  await import("@tensorflow/tfjs");
  const blazeFace = await import("@tensorflow-models/blazeface");
  return await blazeFace.load();
}
