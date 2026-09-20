You are working on my personal software engineering portfolio at **sreejitkar.github.io**.

I want to improve the site without turning it into an over-designed developer portfolio. The goal is:

> **Minimal, lightweight, technically interesting, personal, and memorable.**

Before making changes, inspect the existing codebase and understand the current structure, styling, typography, responsiveness, and content. Preserve anything that is already working well.

### Overall design direction

Keep the current minimalist philosophy. Do NOT introduce:
- Heavy animations
- Particle effects
- Gradient-heavy backgrounds
- Excessive cards
- Skill bars
- Giant technology logos
- Generic “developer portfolio” visual patterns
- Unnecessary JavaScript
- Heavy UI libraries or dependencies

The site should remain extremely fast and lightweight.

Use **typography, whitespace, hierarchy, and subtle interactions** as the primary design elements.

---

## 1. Redesign the hero section

The current opening is too résumé-like.

Instead, make the hero feel more personal and memorable.

Use a headline along the lines of:

**“I like complicated systems. I like making them simpler.”**

Follow it with a concise technical descriptor:

**Software Engineer · Distributed Systems · Infrastructure · Observability**

The hero should immediately communicate both:
1. What I do
2. How I think

Keep the hero visually clean with plenty of whitespace.

---

## 2. Rewrite the About section

Replace the current résumé-style introduction with a short personal essay.

The tone should be thoughtful, confident, curious, and slightly playful—not corporate.

Use this as the general direction:

> I’m a software engineer who enjoys understanding how things work under the hood. I’m particularly drawn to distributed systems, cloud infrastructure, observability, and system architecture—especially the messy problems that appear when software operates at scale.
>
> I enjoy thinking about how thousands of services, machines, metrics, logs, and events come together to form reliable systems. I like designing infrastructure that is scalable, fault-tolerant, observable, and boring in production—because in infrastructure, boring is usually a compliment.
>
> I’m also interested in the intersection between engineering and economics. I enjoy looking at a system and asking not just “Can we build this?” but “Do we need to build it this way?” There’s something satisfying about taking an expensive or overly complicated architecture, understanding where the complexity comes from, and finding a simpler approach.
>
> Outside technology, I read, sing, travel, ride my bike to unfamiliar places, and I’m learning piano. I tend to go down rabbit holes—sometimes technical, sometimes completely unrelated.
>
> **I build software, think about systems, and spend a lot of my time being curious about how things work.**

Feel free to refine the wording slightly so it fits the visual design and existing voice of the site.

---

## 3. Add a “Currently interested in” section

Create a compact section rather than a conventional skills grid.

Heading:

**Currently interested in**

Display these as simple inline text/tags:

- Distributed Systems
- Observability
- Kubernetes
- Cloud Infrastructure
- Event-Driven Architecture
- System Design
- Engineering Economics
- Agentic AI

Avoid visual “skill bars” or percentage indicators.

Add a small line underneath:

> Lately I’ve been thinking about how agentic AI can operate infrastructure safely, how observability systems should evolve, and what happens when you push distributed systems to their limits.

---

## 4. Add a “Selected Work” section

Create a section showcasing 3–4 meaningful engineering projects/areas.

Do NOT make these generic project cards.

Use a clean editorial/list-based layout.

Possible entries:

### Making observability cheaper at scale
**Metrics · Datadog · Grafana · Kubernetes**

Short description:
> Exploring how large-scale metrics pipelines can be made more efficient, observable, and cost-effective.

### Modernising legacy monitoring
**Distributed Systems · Kubernetes · High Availability**

Short description:
> Re-thinking legacy monitoring infrastructure as a distributed, containerised and highly available platform.

### Observability Infrastructure
**Prometheus · Grafana · Alertmanager · OpenTelemetry**

Short description:
> Building the systems that help engineers understand what is happening across large-scale infrastructure.

### Notes on Systems
**Architecture · Reliability · Infrastructure**

Short description:
> A growing collection of things I’ve learned while building and thinking about distributed systems.

Keep the descriptions short.

If the existing site already has project content, preserve accurate existing information and adapt it to this structure rather than inventing new projects.

---

## 5. Add a “Now” section

Create a small section that makes the website feel like a snapshot of the current version of me.

Heading:

**Now**

Example content:

> Building distributed infrastructure at scale.  
> Learning piano.  
> Reading about systems and architecture.  
> Exploring new places on two wheels.  
> Thinking about useful applications of AI in infrastructure.

Keep this visually small.

---

## 6. Improve navigation

Keep navigation extremely simple.

Something like:

**About · Work · Notes · Now · Contact**

Navigation should remain accessible without taking significant screen space.

On mobile, ensure it remains clean and usable.

---

## 7. Typography and visual hierarchy

Prioritise typography over decorative UI.

The page should have:
- Strong but not enormous headings
- Comfortable line lengths
- Generous whitespace
- Clear section hierarchy
- Subtle dividers where useful
- Excellent mobile typography
- A restrained colour palette

The site should feel closer to a **well-designed personal publication** than a SaaS landing page.

---

## 8. Subtle interactions

Add interaction only where it improves usability.

Examples:
- Subtle hover states on project links
- Small transitions on navigation
- Underline/opacity transitions
- Smooth scrolling if appropriate

Avoid animation for animation's sake.

Respect `prefers-reduced-motion`.

---

## 9. Performance requirements

Performance is important.

Before adding any dependency, ask whether it is actually necessary.

Prefer:
- CSS over JavaScript
- System fonts or an already-existing lightweight font setup
- Static HTML/content where possible
- Minimal client-side JavaScript
- Lazy loading where appropriate

Do not introduce large UI frameworks simply for visual effects.

The final site should remain highly performant on mobile and desktop.

---

## 10. SEO and accessibility

While making the visual changes, also improve:
- Semantic HTML
- Heading hierarchy
- Accessible navigation
- Link labels
- Image alt text
- Page title
- Meta description
- Open Graph metadata
- Keyboard navigation
- Colour contrast
- Reduced-motion support

Do not compromise the minimalist design for SEO.

---

## 11. Most important design principle

The final result should NOT look like:

> “Another software engineer portfolio.”

It should feel like:

> **A thoughtful engineer who is obsessed with systems, enjoys making complicated things simpler, and has a life outside of code.**

The website should communicate personality through **writing and restraint**, not through visual gimmicks.

Before finishing:
1. Inspect the site at desktop, tablet, and mobile widths.
2. Remove anything that feels unnecessary.
3. Check for excessive spacing or visual clutter.
4. Ensure the page still loads quickly.
5. Ensure all existing links and functionality continue to work.
6. Keep the implementation clean and maintainable.

Do not rewrite factual details about my experience unless they already exist in the code/content or are explicitly provided above.