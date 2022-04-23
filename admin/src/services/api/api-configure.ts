import Axios from "axios";

import useSWR from "swr";

const api = Axios.create({
  baseURL: "http://192.168.2.172:8000/",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
});

const axiosFetcher = (url: string) => api.get(url).then((res) => res.data);

export function useSwrFetcher(url: string) {
  const { data, error } = useSWR(url, axiosFetcher);

  return { data, error };
}

export default api;
