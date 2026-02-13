# Engineering Sandbox

## What's up?

This repository is about creating an environment for EPF students to try out GitHub features alongside engineering skills, planning and designing on one hand and collaborating and solving technical issues together on the other hand.

## A word of warning

```
Most of the textual content below has been generated from transcripts of classes with 2025's 5A.

It has then been reviewed to match pedagogical expectations.
```

## Skills

- **Methodological rigor**: planning and scoping to deliver on commitments
- **Technical collaboration**: building and maintaining a system collectively

### Methodological rigor

Includes: planning & estimation, documentation structure, ticket management, data quality & specifications, scope management, output vs outcome, quality standards

**Essence**: Know how to estimate (×2 +10%), structure work (Why/What/How/When), define realistic scope, aim for impact (outcome) rather than production (output), and maintain professional quality standards.

### Technical collaboration

Includes: efficiency vs effectiveness, technical documentation & architecture, GitHub & version control, collective code ownership, centralization vs fragmentation, tool mastery, architecture & technical debt, review & team blocking

**Essence**: Work as a team on shared codebase (Git/PRs), create documented and maintainable architecture, depersonalize code, avoid fragmentation, master collaborative tools, manage technical debt.

## Evaluation grid

|                                                |                                                                                    | Resit À reprendre                                                                                                     | Needs Work À travailler                                                                                                                                                  | Basic Bases                                                                                                                                                                         | Solid Solide                                                                                                                                                                                                  | Outstanding Remarquable                                                                                                                                                                                                                          |
| ---------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Planning and scoping to deliver on commitments | Expectations Attentes                                                              | Student cannot estimate realistic task durations or define achievable project scope. No planning structure visible.   | Student creates basic planning (Gantt/Trello) but estimates are unrealistic (no ×2 +10% buffer). Scope is poorly defined or changes constantly without client alignment. | Student creates structured planning with realistic estimates (×2 +10% applied). Tickets follow Why/What/How/When structure. Scope is defined but may drift without proper tracking. | Student maintains accurate planning throughout project. Adjusts estimates based on reality. Scope changes are documented and validated with the fictive client. Focuses on outcomes rather than just outputs. | All the above + Student proactively identifies risks in planning, communicates scope trade-offs transparently, maintains professional quality standards (documentation, no typos in client materials), and delivers on commitments consistently. |
|                                                | Observables (Realized / Not realized) Critères observables (Atteint / Non atteint) | No planning tool used or visible. Lab deadlines missed without communication. Autonomy work lacks defined objectives. | Planning tool (Kanban) created but not maintained. Large gaps between planned and actual dates. Lab deliverables incomplete or missing key specifications.               | Planning tool used with structured tickets. Estimates documented. Labs completed with defined scope. Autonomy work has clear objectives and deliverables defined upfront.           | Planning updated regularly. Fictive client validation obtained for scope changes. All labs delivered on time with quality documentation. Autonomy work demonstrates outcome focus.                            | All the above + Planning shows risk mitigation. Fictive client materials are polished (no typos, professional language). Transparency on difficulties documented. Autonomy work exceeds expectations with measurable impact.                     |

|                                                |                                                                                    | Resit À reprendre                                                                                                   | Needs Work À travailler                                                                                                                                                        | Basic Bases                                                                                                                                                                                       | Solid Solide                                                                                                                                                                                                                       | Outstanding Remarquable                                                                                                                                                                                                                                     |
| ---------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Building and maintaining a system collectively | Expectations Attentes                                                              | Student works in isolation without version control or code reviews. No collaborative development practices visible. | Student uses Git but with poor practices (working on main, no PRs, merge conflicts). Code is personalized and difficult for others to modify. Documentation minimal or absent. | Student uses Git with branches and basic PRs. Code is somewhat documented. Participates in code reviews but may block team progress by being the sole reviewer. Basic architecture understanding. | Student uses Git effectively with clean PRs and timely reviews. Code ownership is collective (depersonalized). Technical documentation maintained. Architecture decisions are discussed and documented. Technical debt identified. | All the above + Student proactively improves architecture, manages technical debt strategically, unblocks teammates through collaborative reviews, masters collaborative tools (GitHub/CI/CD), and creates maintainable, well-documented systems.           |
|                                                | Observables (Realized / Not realized) Critères observables (Atteint / Non atteint) | No Git repository or only local work. No evidence of collaboration. Code not shared or inaccessible to team.        | Git used but frequent merge conflicts. PRs rare or non-existent. Code reviews absent. README outdated or missing. Personal coding style prevents collaboration.                | Regular commits with branches. PRs created and merged. Basic code reviews conducted. README exists with setup instructions. Can work on others' code with guidance.                               | Clean Git history with meaningful commits. PRs reviewed by multiple people. Technical documentation updated. Architecture diagrams or decisions documented. Reviews don't block team. Tests written before merging.                | All the above + Architecture refactoring documented. Technical debt tracked and addressed. Collaborative tools mastered (CI/CD pipelines, automated tests). Code quality standards enforced. Team unblocked through proactive reviews and pair programming. |

## Key concepts

# Key concepts

### **1. Efficiency vs Effectiveness**

**Efficiency** is the ratio between effectiveness and safety. Being effective without consideration for sustainability or safety puts the system at risk. Efficiency means being productive without compromising the robustness and maintainability of the system. This is a fundamental concept to avoid burnout - working to exhaustion without a long-term vision.

### **2. Planning and estimation**

**Estimation rule**: multiply the optimistic estimate by 2, then add 10% to get the pessimistic estimate. This rule helps anticipate risks (failures, blockers, unforeseen events). Distinguish total available time from actual working time (meetings, other tasks). Importance of documenting reasons for delays directly in tickets to facilitate future understanding.

### **3. Documentation structure (Design Document)**

**Why - What - How - When**: This structure (also called specifications or requirements document) structures each task:

- **Why**: justification for the work
- **What**: objective to achieve
- **How**: possible solutions and their advocacy (what we do AND what we don't do)
- **When**: timeline estimates

### **4. Professional meeting preparation**

Before each meeting, review: what you worked on, what colleagues worked on, current issues, what needs discussion. Adopt a methodical and factual approach. Update Trello/dashboard BEFORE the meeting to compare forecasts vs reality.

### **5. Agile method and client rhythm**

Regular meetings with the client (every 2 weeks) serve as the "final arbiter" to validate progress. After each client meeting, set objectives for the next one. The client must validate what is good, what is not, and what remains to be done. Create mock-ups when the client doesn't have a clear idea.

### **6. Ticket and task management**

Create clear and detailed tickets with all necessary details for overall understanding. Subdivide a ticket if multiple tasks are discovered. Avoid being too vague or too precise. Always know: why we're doing it, what we must do, when to deliver it, and **especially what we're not doing**.

### **7. Technical documentation and architecture**

Importance of creating architecture diagrams (even simple ones: input, output, constraint). A picture is worth a thousand words. Document for two audiences: end users AND developers taking over the project. Identify stakeholders and their specific documentation needs.

### **8. Team collaboration and communication**

**Proactive communication**: send messages/audio to the group to inform about modifications, results and problems encountered. **Pair programming**: two brains working together (500% efficiency) - one observes and guides, the other acts. **Presence communication**: notify the team of your availability because the team moves forward with or without each member.

### **9. GitHub and version control**

Use feature branches, merge with main then delete after validation. Create pull requests. Create **GitHub issues** to document improvement opportunities, bugs, and what works well. Use tags for versioning.

### **10. Data quality and specifications**

**Crucial lesson**: always ask to see the data BEFORE committing to a project. Project specifications must be clear from the start. If the team discovers a gap between expectations and reality, adapt the roadmap quickly and communicate diplomatically with the client.

### **11. Presentation: double triangle technique**

Structure going from global to technical:

- **First triangle (broad → precise)**: first present the big picture with technical foundation, then features with technical tools, finally technical specifications responding to specific challenges
- **Second technical triangle**: will likely be smaller than the global part
- Address a single person, use structured images

### **12. Professional justification and transparency**

In case of difficulties or delays: be transparent, acknowledge weaknesses upfront, propose improvement recommendations for each problem, highlight what worked well. Show your capacity for progress rather than just your current technical level.

### **13. Team communication and crisis management**

**Gentle communication** is essential when a member disappears or becomes desynchronized. Don't wait for a problem to worsen: intervene quickly but with kindness. Establish presence/availability rituals. If a member is absent, the team must continue moving forward while maintaining contact.

### **14. Collective code ownership**

**"The code doesn't belong to me"**: crucial transition from personal development to team code. Code must be **depersonalized** so that each member can contribute without psychological barriers. This requires naming conventions, clear comments, coherent structure, and acceptance that "my" code becomes "our" code.

### **15. Centralization and fragmentation**

Avoid **work fragmentation**: when each member works in their own repository or environment, integration becomes nightmarish. Establish from the start **a central repository** with clear folder structure. Define who is responsible for what, where to push their work, and how to integrate it.

### **16. Tool mastery before use**

Don't assume students master Trello, GitHub, or any other tool even after a presentation. **Teach concrete usage** with examples, templates, and follow-up. A poorly understood tool becomes a burden rather than a help. Verify understanding through guided practice.

### **17. Scope management and realism**

**Clean house** regularly: what are we **really** going to do? Who is **really** available? When do we draw the conclusion? Abandoning unproductive paths is not failure but mature management. Document what is abandoned and why.

### **18. Client relationship and autonomy**

When the client is **too lax** or absent, the team must make validation decisions themselves (constructive "mutiny"). But beware: document these decisions and their justifications to protect the team. Propose validation milestones to the client even if they don't request them.

### **19. Professionalism and punctuality**

**Respect schedules**: 10 minutes late without notification is professionally unacceptable. Communicate proactively in case of unforeseen events. Propose meetings with **agenda shared in advance** to allow preparation. Being on time means respecting others' time.

### **20. Output vs Outcome**

**Output** = produced result (lines of code, completed tickets, delivered features). **Outcome** = real impact, problems solved, value created for the user. A burndown chart can mask reality: completing many poorly designed tickets creates no value. The **success criteria** are not "produce code" but "solve the client's problem".

### **21. Quality standards and proofreading**

**Proofread multiple times** before delivering. Spelling errors in the client's name or euphemisms ("quite unfamiliar" instead of "completely lost") harm credibility. Establish explicit **quality standards** for the team. Avoid "etc." or "to be honest" in professional deliverables.

### **22. Architecture and technical debt**

Working in an **unclean architecture** with poor knowledge of the project/language generates conflicts and blockages. Sometimes necessary to "hack" the architecture to rebuild it properly. Create **architecture diagrams** even simple ones. If the diagram is too large for the screen, present a zoomed-out view then zoom in on each step.

### **23. Presentation and visual support**

**Get out of slides**: present the **live Kanban**, the **mockup itself**, the **dashboard running locally**. Use **screenshots** to show real tools. Structure "where you come from → where you're going" (motivation grid). Integrate tools in slides with justification: "why each tool for which specific problem".

### **24. Review and team blocking**

Don't **wait indefinitely** for a member to do their review. Establish review deadlines (e.g., 24h) after which you can merge with another member's approval. PR blocking by a reviewer's absence paralyzes the entire team.

### **25. Sincerity and vulnerability**

**Don't use euphemisms** to mask difficulties. Say "we were completely lost" rather than "quite unfamiliar". Showing **adaptation capacity** in the face of difficulties is an engineering skill. Using Figma AI + ChatGPT/Cursor when you don't know how to design an interface is an intelligent solution, not a weakness.
