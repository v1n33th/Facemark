import TimeSheetPage from "../components/pages/time-sheet/time-sheet-page";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";

function Timesheet() {
  return (
    <>
      <AppBar position="static">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Typography
              variant="h6"
              noWrap
              component="div"
              sx={{ mr: 2, display: { xs: "none", md: "flex" } }}
            >
              FACE MARK
            </Typography>
          </Toolbar>
        </Container>
      </AppBar>
      <TimeSheetPage />
    </>
  );
}

export default Timesheet;
