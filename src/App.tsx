import React, { useState } from "react";
import "./App.css";
import {
  AppBar,
  Grid,
  Tab,
  Tabs,
  TextField,
  Toolbar,
  Typography,
  Button,
} from "@mui/material";
import { makeStyles } from "@mui/styles";
import { GithubData, LangName, Langs } from "./types";
import { searchCodeRepo } from "./api";
import { GithubDataTable } from "./GithubDataTable";

const useStyles = makeStyles((theme) => ({
  searchInput: {
    flex: 1,
  },
  searchButton: {},
}));

function App() {
  const [lang, setLang] = useState<Langs>(Langs.JavaScript);
  const [q, setQ] = useState("");
  const [data, setData] = useState<GithubData[]>([]);
  const classes = useStyles();

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
              <Grid container direction="row" item xs={12}>
                <TextField
                  label="Search phrase"
                  variant="outlined"
                  value={q}
                  className={classes.searchInput}
                  onChange={(e) => setQ(e.target.value)}
                  onKeyPress={async (e) => {
                    if (e.key === "Enter") {
                      e.preventDefault();
                      const data = await searchCodeRepo(lang, q);
                      setData(data);
                    }
                  }}
                />
                <Button
                  variant="contained"
                  size="large"
                  color="primary"
                  className={classes.searchButton}
                  onClick={async () => {
                    const data = await searchCodeRepo(lang, q);
                    setData(data);
                  }}
                >
                  Search
                </Button>
              </Grid>
              <Grid item xs={12}>
                <GithubDataTable data={data} />
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
