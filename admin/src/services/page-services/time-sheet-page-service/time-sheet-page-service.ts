import { format } from "date-fns";

export function formatDate(
  date: Date,
  dateFormat = "yyyy-MM-dd'T00:00:00.000000'"
) {
  return format(date, dateFormat);
}
