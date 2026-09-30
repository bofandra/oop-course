# Accessibility Guide

This repository is primarily text- and code-based. The goal of this guide is to keep the course usable for learners who rely on keyboard navigation, screen readers, zoom, high-contrast settings, or reduced visual complexity.

## Learner guidance

The course can be used directly in GitHub or through Google Colab.

For a lower-friction path:

1. begin with [Start Here](START_HERE.md);
2. use the [Colab notebook index](COLAB.md);
3. increase browser/Colab zoom or font size as needed;
4. use the Markdown course notes when notebook rendering is difficult;
5. use the module README, exercises, assignment, and mastery checks as text alternatives to notebook navigation.

## Content authoring rules

When adding or editing course material:

- use descriptive headings in logical order;
- use meaningful link text instead of "click here";
- keep code examples small and explain their purpose in surrounding text;
- do not rely on color alone to communicate meaning;
- provide text explanations for diagrams and visual relationships;
- add useful alt text to images if images are introduced;
- keep tables simple enough to read linearly;
- avoid decorative Unicode that carries essential meaning without a text explanation;
- avoid autoplaying audio/video or time-dependent interaction as required course content;
- keep essential instructions available as plain text.

## Diagrams

ASCII or text diagrams are used throughout the course because they remain readable without image rendering.

When a richer diagram is added, include a nearby text description that communicates the same learning point.

Example:

```text
Car
  └── has-a → Engine
```

The surrounding explanation should still state the relationship in words.

## Notebooks

Notebook cells should remain understandable when read from top to bottom.

Authors should:

- introduce the goal of a code cell before or immediately after it;
- avoid making a screenshot the only source of required information;
- keep learner TODO instructions in Markdown or comments;
- avoid hidden setup steps;
- preserve sequential execution.

## Assessment accessibility

Assessment quality should depend on understanding OOP concepts, not on visual speed or familiarity with a specific interface.

Facilitators may adapt presentation or timing to learner needs as long as the assessed learning outcome is preserved.

## Contributions

Accessibility improvements are welcome. Use the repository issue templates or follow [CONTRIBUTING.md](CONTRIBUTING.md).
