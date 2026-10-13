(() => {
  const root = document.getElementById("research");
  if (!root) return;

  const controls = root.querySelector(".jl-research-controls");
  const search = root.querySelector("#research-search");
  const buttons = [...root.querySelectorAll("button[data-tag]")];
  const count = root.querySelector("#research-count");
  const reset = root.querySelector("#research-reset");
  const empty = root.querySelector(".jl-research-empty");
  const years = [...root.querySelectorAll("[data-research-year]")];
  const normalize = (text) =>
    text
      .normalize("NFKD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase();
  const papers = years.flatMap((year) =>
    [...year.querySelectorAll(".jl-paper")].map((element) => ({
      element,
      tags: element.dataset.tags.split("|"),
      text: normalize(`${year.dataset.researchYear} ${element.textContent}`),
    }))
  );
  let selected = "";

  function filter() {
    const terms = normalize(search.value).trim().split(/\s+/).filter(Boolean);
    let visible = 0;
    papers.forEach((paper) => {
      const matches = (!selected || paper.tags.includes(selected)) && terms.every((term) => paper.text.includes(term));
      paper.element.hidden = !matches;
      if (matches) visible += 1;
    });
    years.forEach((year) => {
      year.hidden = ![...year.querySelectorAll(".jl-paper")].some((paper) => !paper.hidden);
    });
    buttons.forEach((button) => button.setAttribute("aria-pressed", String(button.dataset.tag === selected)));
    count.textContent = visible === papers.length ? `${visible} papers` : `${visible} of ${papers.length} papers`;
    empty.hidden = visible !== 0;
    reset.hidden = !selected && !search.value;
  }

  search.addEventListener("input", filter);
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      selected = button.dataset.tag;
      filter();
    });
  });
  reset.addEventListener("click", () => {
    selected = "";
    search.value = "";
    filter();
    search.focus();
  });
  filter();
  controls.hidden = false;
})();
