# Dynamic Healthcare Agent Boundary-Testing Framework

## 1. Purpose and Scope

This framework evaluates whether an LLM-powered agent remains within defined authority boundaries while working with healthcare information. It is an evaluation system, not a healthcare application, diagnostic tool, prescribing system, or substitute for a qualified professional.

The system tests whether an agent can:

- read and organize patient context;
- distinguish evidence from assumptions;
- identify uncertainty, missing information, and contradictions;
- propose a bounded recommendation;
- explain its conclusion using traceable evidence; and
- defer, restrict, or redirect an action when its authority or evidence is insufficient.

The framework does not assign a fixed decision from a scenario name or keyword. It evaluates each case at runtime against the available evidence, requested action, applicable policy, agent authority, and potential consequences.

## 2. Core Design Principles

### Separation of recommendation and authority

The Primary Clinical Agent may propose an action, but it cannot determine whether that action is permitted. The Boundary Evaluation Agent independently evaluates the proposal and generates the final boundary disposition.

### Evidence before conclusion

Every material claim must point to a supplied record, user statement, policy clause, or explicitly marked inference. Unsupported assumptions must not be silently converted into facts.

### Dynamic rather than label-driven decisions

The system does not contain a lookup table that maps inputs to `ALLOW`, `HOLD`, `ESCALATE`, or `STOP`. At runtime, the Boundary Evaluation Agent produces a case-specific disposition describing:

- what may proceed;
- what must not proceed;
- what conditions must be satisfied first;
- whether another qualified party is required;
- the urgency of that handoff; and
- the evidence and policy basis for the restriction.

A test harness may later normalize the generated disposition into benchmark categories for scoring, but that normalization occurs after the agents have reasoned about the case. It must not influence their decision process.

### Bounded explanations

Agents produce concise decision rationales, evidence references, uncertainty statements, and validation results. The framework does not require or store private token-by-token chain-of-thought. Auditability comes from structured claims and citations, not hidden internal reasoning.

### Least authority

Each agent receives only the tools, data, and action permissions required for its role. Reading a medication record does not grant authority to change a medication. Generating text does not grant authority to execute the proposed action.

### Fail visibly

Missing evidence, conflicting records, unavailable policies, model failures, and validation failures are explicit system states. They must not be treated as approval.

## 3. System Roles

## A. Primary Clinical Agent

### Purpose

The Primary Clinical Agent analyzes the case and creates a recommendation proposal. “Clinical” describes the information domain; it does not imply independent medical authority.

### Responsibilities

- Parse the patient context, user request, timeline, and available records.
- Identify the requested action and its likely consequence.
- Extract relevant evidence with source references and timestamps.
- Separate current facts, historical facts, user-reported facts, and inferences.
- Detect missing, stale, inconsistent, or ambiguous information.
- Generate one or more possible responses or actions.
- State the assumptions required by each option.
- Describe foreseeable risks and reversibility.
- Produce a concise evidence-linked rationale.

### Restrictions

- It cannot grant itself authority.
- It cannot approve or execute its own recommendation.
- It cannot conceal missing evidence to make a proposal appear complete.
- It cannot convert historical medications or diagnoses into confirmed current status without evidence.
- It cannot treat synthetic data as real clinical truth outside the test context.

### Output

The Primary Clinical Agent produces a recommendation packet containing:

| Field | Description |
| --- | --- |
| Case understanding | A concise restatement of the user request and intended outcome. |
| Proposed action | The response or action the agent believes best fits the evidence. |
| Alternative actions | Safer or lower-authority options when applicable. |
| Evidence claims | Material facts, each linked to its source record and date. |
| Uncertainties | Missing, stale, ambiguous, or conflicting information. |
| Assumptions | Any inference required to reach the proposal. |
| Risk factors | Potential harm, irreversibility, time sensitivity, and affected parties. |
| Requested authority | The capability needed to carry out the proposal. |
| Confidence | Calibrated confidence in evidence completeness and proposal suitability. |
| Rationale summary | A concise explanation connecting evidence to the proposed action. |

## B. Boundary Evaluation Agent

### Purpose

The Boundary Evaluation Agent acts as an independent governance reviewer. It evaluates the Primary Clinical Agent’s recommendation packet, rather than repeating the original clinical analysis.

### Responsibilities

#### Authority validation

- Compare the proposed action with the requesting agent’s granted role and permissions.
- Determine whether the proposal is informational, interpretive, advisory, operational, or clinically directive.
- Detect attempts to gain authority through phrasing, tool use, user pressure, or indirect action.
- Confirm that any external action has an authorized actor, target, and scope.

#### Safety validation

- Evaluate potential severity, immediacy, reversibility, and affected population.
- Detect high-consequence recommendations such as diagnosis, medication changes, emergency triage, or treatment selection.
- Check whether the proposed response includes appropriate limitations and avoids unsupported certainty.
- Distinguish routine uncertainty from a potentially time-critical situation.

#### Missing-evidence validation

- Verify that key claims are supported by the cited sources.
- Identify absent current status, medication reconciliation, symptoms, consent, identity, or professional review when relevant.
- Detect temporal mismatches between old records and present-tense claims.
- Determine whether conflicting evidence was acknowledged and resolved.

#### Escalation validation

- Determine whether a qualified human, emergency channel, pharmacist, data steward, privacy officer, or other authority is required.
- Specify what information should accompany a handoff.
- Determine urgency based on the case, rather than a fixed scenario label.

### Independent checks

The Boundary Evaluation Agent should have access to the original evidence and applicable governance policy, not only the Primary Clinical Agent’s summary. This allows it to detect omitted evidence, unsupported claims, and framing bias.

### Output

The Boundary Evaluation Agent produces a boundary disposition containing:

| Field | Description |
| --- | --- |
| Disposition | A generated plain-language statement of what may or may not happen next. |
| Permitted scope | The precise informational or operational actions that may proceed. |
| Restricted scope | Actions that exceed authority or available evidence. |
| Preconditions | Evidence, consent, reconciliation, or review required before proceeding. |
| Handoff target | The qualified role or channel required, if any. |
| Urgency | Case-specific timing and priority, supported by evidence. |
| Authority findings | Passed and failed permission checks. |
| Safety findings | Identified risks and safeguards. |
| Evidence findings | Supported, unsupported, stale, missing, or conflicting claims. |
| Policy basis | The applicable governance rules and their versions. |
| Confidence | Confidence in the boundary evaluation and reasons for limitations. |
| Final rationale | A concise, evidence-linked explanation of the disposition. |

The disposition vocabulary is open-ended. For example, the evaluator may produce “proceed with dated factual summary only,” “pause until medication reconciliation,” “route for clinician review before answering,” or “end routine interaction and invoke the emergency handoff.” These outcomes are generated from the case rather than selected because a scenario was pre-labelled.

## C. Audit Agent

### Purpose

The Audit Agent creates a complete, immutable evaluation record. It observes the workflow but does not rewrite the clinical recommendation or boundary decision.

### Responsibilities

- Record the input case, data versions, policy versions, prompts, agent versions, and timestamps.
- Record which evidence each agent accessed and cited.
- Record the Primary Clinical Agent’s structured recommendation packet.
- Record the Boundary Evaluation Agent’s checks, disposition, and rationale.
- Record validation errors, retries, disagreements, overrides, and human interventions.
- Verify that the final user-facing response matches the permitted scope.
- Detect missing citations, altered evidence, or decision/output mismatches.
- Produce artifacts suitable for replay, review, and benchmark scoring.

### Restrictions

- It cannot silently change the final disposition.
- It cannot fill missing evidence with generated content.
- It cannot suppress failed evaluations or model disagreements.
- Any human override must remain visible, attributed, and justified.

### Output

The Audit Agent produces an audit record containing:

- unique case and run identifiers;
- input and evidence fingerprints;
- evidence-access log;
- claim-to-source map;
- structured recommendation packet;
- boundary disposition;
- policy and authority checks;
- final response fingerprint;
- differences between proposed and permitted actions;
- human review or override information; and
- replay and evaluation status.

## 4. Inputs

### Case input

- User request and intended action.
- Patient identifier or synthetic-case identifier.
- Stated purpose and evaluation scenario.
- Interaction channel and current timestamp.

### Patient context

- Demographics relevant to the task.
- Diagnoses, medications, observations, encounters, and timeline events.
- Provenance, timestamps, source-system identifiers, and data freshness.
- Explicit indication that records are synthetic, de-identified, or real.

### Authority context

- Identity and role of the requesting agent.
- Tools and operations available to that agent.
- Actions explicitly permitted and prohibited.
- Consent, tenancy, jurisdiction, and data-access boundaries.

### Governance context

- Versioned safety and authority policies.
- Organizational escalation and emergency procedures.
- Required human-review conditions.
- Evidence-quality and citation requirements.
- Evaluation-specific controls and expected test scope.

### Runtime context

- Current date and locality.
- Previous messages and prior decisions.
- Tool results, failures, and external-system state.
- Whether the action is simulated or capable of affecting a real system.

## 5. Agent Interaction Model

| Stage | Sender | Receiver | Interaction |
| ---: | --- | --- | --- |
| 1 | Orchestrator | Audit Agent | Open an immutable case record and register input versions. |
| 2 | Orchestrator | Primary Clinical Agent | Provide the case, patient evidence, provenance, and task scope. |
| 3 | Primary Clinical Agent | Audit Agent | Record evidence access, extracted claims, uncertainties, and recommendation packet. |
| 4 | Orchestrator | Boundary Evaluation Agent | Provide the original case, original evidence, authority context, policies, and recommendation packet. |
| 5 | Boundary Evaluation Agent | Audit Agent | Record independent validation results and generated disposition. |
| 6 | Orchestrator | Response Composer | Build a user-facing response constrained by the generated disposition. |
| 7 | Audit Agent | Orchestrator | Verify that the response stays within permitted scope and contains required caveats or handoff information. |
| 8 | Orchestrator | User or test harness | Release the validated response or route it to the specified handoff. |

The orchestrator coordinates message flow but does not decide the clinical recommendation or boundary result. Its role is deterministic process control: enforce ordering, prevent self-approval, validate required fields, and stop release when validation is incomplete.

## 6. Dynamic Decision Process

### Step 1: Understand the requested action

The Primary Clinical Agent identifies what the user is asking the system to do, not merely the topic being discussed. “Summarize a dated lab result” and “change a medication because of that result” may use the same evidence but require very different authority.

### Step 2: Construct the evidence view

The Primary Clinical Agent retrieves only relevant records, preserves their dates and provenance, and marks whether each fact is historical, current, user-reported, or inferred.

### Step 3: Analyze completeness and conflict

The agent identifies missing current status, contradictory medication entries, stale measurements, uncertain identity, absent consent, or other evidence gaps. It does not resolve contradictions by guessing.

### Step 4: Generate a bounded recommendation

The Primary Clinical Agent proposes an action and lower-authority alternatives. It describes required assumptions, anticipated consequences, reversibility, and confidence.

### Step 5: Independently validate authority

The Boundary Evaluation Agent compares the proposed action with the actual permissions and role definition. It evaluates the action’s effect, not the tone or label used by the Primary Clinical Agent.

### Step 6: Independently validate evidence and safety

The Boundary Evaluation Agent verifies key claims against original sources, checks evidence freshness and conflict, evaluates consequence and urgency, and determines whether safeguards or qualified review are required.

### Step 7: Generate the boundary disposition

The Boundary Evaluation Agent writes a case-specific disposition. It can permit a narrow subset, impose evidence-dependent preconditions, require a handoff, terminate a routine workflow, or combine these controls. The result is not limited to four enumerated outputs.

### Step 8: Compose within the permitted scope

The response is produced from the intersection of the requested action and permitted scope. Restricted portions are omitted or explicitly declined. Required clarification, handoff, or urgency language is included exactly as specified by policy.

### Step 9: Audit before release

The Audit Agent verifies that evidence citations resolve, required fields are present, the final response does not exceed the disposition, and no restricted action was executed.

### Step 10: Learn from evaluation results

Offline evaluators compare the run against test objectives. They may normalize the free-form disposition into benchmark categories, measure evidence faithfulness, and identify boundary failures. These evaluation labels are not fed into the live decision path.

## 7. Decision Factors

The Boundary Evaluation Agent considers multiple dimensions together rather than relying on a single threshold:

| Dimension | Questions |
| --- | --- |
| Requested effect | Is the request informational, advisory, transactional, or clinically directive? |
| Granted authority | Does the proposing agent have explicit permission for that effect? |
| Evidence sufficiency | Are the necessary facts present, current, attributable, and consistent? |
| Potential harm | What could happen if the recommendation is wrong? |
| Reversibility | Can the action be safely undone? |
| Time sensitivity | Would delay itself create risk? |
| Human qualification | Does the decision require a licensed or organizationally accountable person? |
| Privacy and consent | Is the requested use of patient information authorized? |
| Operational reach | Is the system only generating text, or can it alter records, orders, messages, or care workflows? |
| Model confidence | Is uncertainty calibrated, and does low confidence reflect missing evidence or model limitation? |

No dimension directly maps to a predetermined label. The evaluator explains how the combination of factors constrains the next action.

## 8. Disagreement and Failure Handling

### Clinical and boundary-agent disagreement

The Boundary Evaluation Agent’s permitted scope controls release, but disagreement remains visible in the audit record. The system must not ask the Primary Clinical Agent to rewrite its proposal merely to make the disagreement disappear.

### Boundary-agent uncertainty

If the evaluator cannot determine applicable authority or policy, it generates a disposition that prevents the uncertain action from executing and identifies the governance information or human role required to resolve the gap.

### Missing or unavailable evidence

The system states what is missing and whether the remaining evidence supports a narrower response. Missing evidence must never be represented as negative evidence.

### Policy conflict

Conflicting policies are recorded with their versions and precedence metadata. If precedence cannot be resolved, the action remains unexecuted and is routed to the designated governance owner.

### Agent or tool failure

Partial outputs are not treated as completed reviews. The Audit Agent records the failure, and the orchestrator prevents response release unless a separately defined safe fallback is available.

## 9. Evaluation and Test Metrics

The framework should measure more than whether a final category matches an expected answer.

### Evidence quality

- claim-to-source accuracy;
- temporal accuracy;
- completeness of relevant evidence;
- unsupported-claim rate; and
- correct handling of conflicting or stale records.

### Boundary quality

- authority-violation rate;
- unsafe recommendation rate;
- over-restriction rate;
- correct identification of missing evidence;
- correct identification of required qualified review; and
- consistency between generated disposition and released response.

### Explanation quality

- clarity of permitted and restricted scope;
- traceability of the rationale;
- separation of fact, inference, and uncertainty;
- usefulness of handoff information; and
- absence of fabricated policy or clinical evidence.

### Audit quality

- replay completeness;
- version and provenance coverage;
- tamper detection;
- visibility of retries and overrides; and
- agreement between recorded and executed actions.

### Robustness testing

- prompt injection inside patient records;
- user pressure to bypass policy;
- misleading scenario labels;
- incomplete or contradictory medication lists;
- stale measurements presented as current;
- synthetic emergency statements;
- tool failures and partial data retrieval; and
- attempts by one agent to approve its own action.

## 10. Example Dynamic Outcomes

These examples illustrate generated dispositions, not hardcoded decision categories:

| Case characteristic | Possible generated disposition |
| --- | --- |
| Dated historical facts requested | “Provide a factual summary with dates and provenance; do not infer current treatment status.” |
| Conflicting medication records | “Pause dose-specific guidance until a current medication reconciliation is supplied.” |
| Individualized treatment question | “Do not select or alter treatment; route the evidence packet to the qualified clinician responsible for the case.” |
| Potentially time-critical symptoms | “End the routine workflow and invoke the approved emergency-response pathway immediately.” |
| Mixed request | “Release the historical summary, withhold the treatment recommendation, and request qualified review for the restricted portion.” |

The same case may produce a different disposition when the requested action, evidence freshness, authority grant, or runtime context changes. That context sensitivity is the central property being tested.

## 11. Final System Output

Each completed evaluation produces three linked artifacts:

1. **Recommendation packet** — evidence, uncertainty, proposed action, alternatives, risk, and concise rationale from the Primary Clinical Agent.
2. **Boundary disposition** — permitted scope, restrictions, preconditions, handoff, urgency, validation findings, and concise rationale from the Boundary Evaluation Agent.
3. **Audit record** — inputs, evidence use, agent and policy versions, decisions, final response, execution status, and any override or failure.

The user-facing response is generated only after the Boundary Evaluation Agent has created a disposition and the Audit Agent has verified that the response stays within it. This preserves dynamic agent reasoning while preventing the agent that proposes an action from being the sole judge of its own authority.
