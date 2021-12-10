import React, { useState } from "react";
import "./App.css";
import {
  AppBar,
  Grid,
  Tab,
  Table,
  TableContainer,
  TableHead,
  TableRow,
  TableCell,
  Paper,
  TableBody,
  Tabs,
  TextField,
  Toolbar,
  Typography,
} from "@mui/material";

enum Langs {
  JavaScript = "js",
  CSS = "css",
  HTML = "html",
}

const LangName: Record<Langs, string> = {
  [Langs.JavaScript]: "JavaScript",
  [Langs.CSS]: "CSS",
  [Langs.HTML]: "HTML",
};

function App() {
  const [lang, setLang] = useState<Langs>(Langs.JavaScript);
  const [q, setQ] = useState("");

  return (
    <Grid container direction="column" spacing={3}>
      <Grid item xs={12}>
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              Luigi - VS Code Search
            </Typography>
          </Toolbar>
        </AppBar>
      </Grid>
      <Grid item xs={12}>
        <Grid container direction="row">
          <Grid item xs={2}></Grid>
          <Grid item xs={8}>
            <Grid container direction="column" spacing={3}>
              <Grid item xs={12}>
                <Tabs
                  value={lang}
                  onChange={(_, v) => setLang(v)}
                  aria-label="basic tabs example"
                >
                  <Tab
                    label={LangName[Langs.JavaScript]}
                    value={Langs.JavaScript}
                  />
                  <Tab label={LangName[Langs.CSS]} value={Langs.CSS} />
                  <Tab label={LangName[Langs.HTML]} value={Langs.HTML} />
                </Tabs>
              </Grid>
              <Grid container direction="column" item xs={12}>
                <TextField
                  id="outlined-basic"
                  label="Search phrase"
                  variant="outlined"
                  value={q}
                  onChange={(e) => setQ(e.target.value)}
                />
              </Grid>
              <Grid item xs={12}>
                <TableContainer component={Paper}>
                  <Table sx={{ minWidth: 650 }} aria-label="simple table">
                    <TableHead>
                      <TableRow>
                        <TableCell>Name</TableCell>
                        <TableCell align="right">Path</TableCell>
                        <TableCell align="right">GitHub Link</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {/* {[].map((row) => (
                        <TableRow
                          key={row.name}
                          sx={{
                            "&:last-child td, &:last-child th": { border: 0 },
                          }}
                        >
                          <TableCell component="th" scope="row">
                            {row.name}
                          </TableCell>
                          <TableCell align="right">{row.calories}</TableCell>
                          <TableCell align="right">{row.fat}</TableCell>
                          <TableCell align="right">{row.carbs}</TableCell>
                          <TableCell align="right">{row.protein}</TableCell>
                        </TableRow>
                      ))} */}
                    </TableBody>
                  </Table>
                </TableContainer>
              </Grid>
            </Grid>
          </Grid>
          <Grid item xs={2}></Grid>
        </Grid>
      </Grid>
    </Grid>
  );
}

export default App;
