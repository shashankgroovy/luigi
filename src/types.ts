export enum Langs {
  JavaScript = "js",
  CSS = "css",
  HTML = "html",
}

export const LangName: Record<Langs, string> = {
  [Langs.JavaScript]: "JavaScript",
  [Langs.CSS]: "CSS",
  [Langs.HTML]: "HTML",
};

export type GithubData = {
  name: string;
  path: string;
  url: string;
  html_url: string;
};
