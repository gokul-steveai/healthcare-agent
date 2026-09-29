# Dynamic Multi-Agent Healthcare Boundary Testing Framework

## 1. Purpose

This project is a research and demonstration framework for evaluating how LLM-powered agents behave around healthcare information. It is **not** a healthcare application, clinical decision-support product, diagnostic system, prescribing system, or replacement for professional care.

Synthea data provides a realistic but synthetic environment for testing:

- evidence retrieval and interpretation;
- agent reasoning and limitations;
- authority-boundary recognition;
- uncertainty handling;
- recommendation safety;
- escalation behavior;
- governance enforcement; and
- traceability of the final result.

The framework uses the existing dataset analysis, hero-patient selection, patient timeline, and four boundary scenarios as evaluation assets. The scenarios represent expected benchmark outcomes—`ALLOW`, `HOLD`, `ESCALATE`, and `STOP`—but the agents must not receive the expected outcome as an instruction or select it through a hardcoded scenario rule.

## 2. Architecture Overview

The system separates clinical-context analysis, boundary evaluation, and audit into three agents with distinct authority:

| Agent | Primary function | Authority |
| --- | --- | --- |
| Clinical Analysis Agent | Analyze context and propose a recommendation | May analyze and propose; cannot approve or execute its proposal |
| Boundary Evaluation Agent | Independently evaluate authority, evidence, and safety | May produce a boundary decision; cannot alter source evidence |
| Audit & Traceability Agent | Record and verify the evaluation | May validate trace completeness; cannot silently change the decision |

The surrounding orchestration and governance layers provide controlled data access, policy context, message routing, validation, and human-review hooks. They do not replace agent reasoning with fixed medical or boundary rules.

### Logical flow

1. The orchestrator receives patient context and a user request.
2. The Clinical Analysis Agent retrieves relevant evidence and proposes a response or action.
3. The Boundary Evaluation Agent reviews the proposal against original evidence, uncertainty, authority, and safety context.
4. The Boundary Evaluation Agent dynamically produces one of the benchmark outcomes.
5. The Audit & Traceability Agent records the claims, evidence, checks, decision, and final response.
6. A response composer releases only content permitted by the boundary decision.
7. Human review is invoked when required by the generated decision or research protocol.

### Separation-of-duty rule

No agent may both propose and approve the same action. The Clinical Analysis Agent cannot set the final boundary outcome. The Boundary Evaluation Agent must have independent access to the case evidence and must not rely solely on the Clinical Agent’s summary.

## 3. Design Principles

### Dynamic reasoning

The agents evaluate the actual user request, evidence, uncertainty, authority, and consequence at runtime. A scenario label, diagnosis keyword, medication name, or single threshold must not directly determine the outcome.

### Evidence-grounded outputs

Material claims must identify their evidence source and timestamp. Historical data must not be presented as current status unless the data supports that conclusion.

### Explicit uncertainty

Missing, conflicting, stale, or ambiguous information is a first-class output. Agents must not silently fill gaps with plausible clinical assumptions.

### Least authority

The Clinical Agent receives analysis authority, not treatment authority. Reading a medication record does not authorize changing a medication. Producing a recommendation does not authorize executing it.

### Independent governance review

The Boundary Agent evaluates the proposed effect of an action, not merely its wording. Rephrasing a treatment instruction as “education” must not bypass authority review.

### Explainability without private chain-of-thought

The framework records structured decision rationale, evidence references, assumptions, uncertainties, validation checks, and conclusions. It does not require disclosure or storage of private token-by-token model chain-of-thought. This provides reproducible explainability while avoiding reliance on unverifiable hidden reasoning.

### Fail visibly

Retrieval failures, policy conflicts, missing evidence, schema errors, and model uncertainty remain visible. Failure to complete an evaluation must never be treated as permission to proceed.

## 4. Agent 1 — Clinical Analysis Agent

### 4.1 Purpose

The Clinical Analysis Agent creates an evidence-based understanding of the case and proposes a bounded recommendation. “Clinical” refers to the information domain, not independent medical authority.

### 4.2 Responsibilities

- Read the patient context and user request.
- Determine the actual action requested by the user.
- Analyze patient history, diagnoses, medications, observations, labs, and encounters.
- Retrieve only evidence relevant to the request.
- Preserve evidence provenance and dates.
- Distinguish recorded facts, user-reported facts, assumptions, and inferences.
- Identify missing, stale, inconsistent, or conflicting information.
- Generate a proposed recommendation and safer alternatives when applicable.
- Describe potential risks, reversibility, and time sensitivity.
- Explain confidence and the reasons for that confidence.
- Produce a concise, evidence-linked rationale.

### 4.3 Limitations

The Clinical Analysis Agent must not:

- assign the final boundary decision;
- claim authority it has not been granted;
- prescribe, diagnose, or change care merely because records are available;
- treat a historical medication entry as a verified current regimen;
- hide contradictory evidence;
- execute external actions; or
- infer that missing information is normal or negative.

### 4.4 Input contract

| Input | Description |
| --- | --- |
| Patient context | Structured demographics, timeline, conditions, medications, observations, encounters, and provenance |
| User request | The current question or requested action |
| Task context | Research scenario, timestamp, data freshness, and whether execution is simulated |
| Agent authority | Explicit capabilities and restrictions of the Clinical Agent |
| Retrieval access | Read-only access to permitted synthetic patient evidence |

Conceptual input shape:

- `patient_context`: the patient facts and source metadata;
- `user_request`: the user’s request in its original wording;
- `task_context`: current evaluation and runtime context; and
- `authority_context`: the agent’s role and limitations.

### 4.5 Output contract

| Output field | Required content |
| --- | --- |
| Analysis | Concise interpretation of the request and relevant patient context |
| Evidence | Claim-level evidence references with source, date, field, and value |
| Reasoning summary | A bounded explanation connecting evidence to the proposal |
| Uncertainties | Missing, stale, ambiguous, or conflicting information |
| Recommendation | Proposed response or action, clearly separated from facts |
| Alternatives | Lower-risk or lower-authority options when available |
| Risks | Potential harm, reversibility, urgency, and affected parties |
| Required authority | Authority or professional qualification needed to act |
| Confidence | Calibrated level plus evidence-based justification |
| Assumptions | Explicit assumptions used in forming the proposal |

The required project fields—`analysis`, `evidence`, `reasoning`, `uncertainties`, `recommendation`, and `confidence`—are retained. The additional fields improve boundary evaluation and auditability.

### 4.6 Confidence model

Confidence should not be a decorative score. It should separately address:

- confidence that the correct evidence was retrieved;
- confidence that the evidence is current and complete;
- confidence in the factual analysis;
- confidence that the recommendation fits the available evidence; and
- known reasons the confidence could be wrong.

High confidence in evidence extraction does not imply authority to act.

## 5. Agent 2 — Boundary Evaluation Agent

### 5.1 Purpose

The Boundary Evaluation Agent independently determines whether the Clinical Agent’s proposal may proceed, must wait for information, requires qualified review, or must end in favor of an urgent safety pathway.

It generates one of four benchmark-compatible outcomes:

- `ALLOW`
- `HOLD`
- `ESCALATE`
- `STOP`

These are possible outputs, not scenario rules. The outcome must be produced from a complete runtime evaluation.

### 5.2 Responsibilities

- Evaluate the complete Clinical Agent output.
- Independently inspect the original request and evidence.
- Detect unsupported, missing, stale, or conflicting evidence.
- Detect insufficient patient or task context.
- Validate the Clinical Agent’s actual authority.
- Identify safety concerns and irreversible consequences.
- Detect potentially urgent or emergency situations.
- Determine whether human or specialist review is required.
- Define permitted and prohibited portions of a mixed request.
- Generate the boundary decision and evidence-linked rationale.
- Specify required actions, preconditions, urgency, and handoff target.

### 5.3 Evaluation dimensions

The Boundary Agent considers the dimensions together; none is a hardcoded outcome trigger.

| Dimension | Evaluation questions |
| --- | --- |
| Requested effect | Is the request factual, interpretive, advisory, transactional, or clinically directive? |
| Evidence sufficiency | Is required evidence present, relevant, current, attributable, and consistent? |
| Uncertainty | Could unresolved uncertainty materially change the safe response? |
| Authority | Is the proposed action within the Clinical Agent’s explicit role? |
| Potential harm | What could happen if the proposal is wrong? |
| Reversibility | Can the proposed action be safely undone? |
| Time sensitivity | Could delay or continued interaction create additional risk? |
| Human qualification | Does the action require a licensed or accountable person? |
| Privacy and consent | Is use of the patient context permitted for this test? |
| Operational reach | Does the proposal only produce text, or could it alter records, orders, messages, or care? |
| Explanation quality | Are claims traceable and limitations stated? |

### 5.4 Dynamic outcome formation

The Boundary Agent first creates findings for evidence, authority, safety, urgency, and required oversight. It then selects the outcome that best represents the combined findings.

The system must not implement rules such as:

- “If diabetes, then escalate.”
- “If information is missing, always hold.”
- “If an emergency keyword occurs, always stop.”
- “If confidence exceeds a fixed score, allow.”

Instead, the agent must explain why the missing information matters, why the requested effect exceeds authority, why delay is or is not acceptable, and why the selected outcome is proportionate to the case.

### 5.5 Outcome semantics

The semantics provide a shared evaluation vocabulary without prescribing fixed detection rules.

| Outcome | Runtime meaning |
| --- | --- |
| ALLOW | The requested response is within authority and sufficiently supported, possibly with explicit scope limits |
| HOLD | The action must pause because resolvable evidence, identity, consent, or context is missing or conflicting |
| ESCALATE | A qualified human or higher-authority role must evaluate or own the decision |
| STOP | The routine workflow must end because continuing it would conflict with an urgent safety or governance requirement |

A mixed request may include a narrow permitted component and a restricted component. The Boundary Agent should state both, while selecting the outcome that controls the consequential portion.

### 5.6 Input contract

The Boundary Agent receives:

- the original user request;
- the original patient evidence and provenance;
- the complete Clinical Agent output;
- the Clinical Agent’s authority definition;
- versioned governance and safety policy;
- current runtime context; and
- available human or emergency handoff routes.

Providing original evidence prevents the Boundary Agent from inheriting omissions or framing errors from the Clinical Agent.

### 5.7 Output contract

| Output field | Required content |
| --- | --- |
| Boundary decision | Dynamically generated `ALLOW`, `HOLD`, `ESCALATE`, or `STOP` |
| Boundary reasoning | Concise rationale linked to evidence, uncertainty, authority, and safety findings |
| Identified risks | Specific risks, their evidence, severity, and uncertainty |
| Required actions | Preconditions, clarification, handoff, or emergency process required next |
| Permitted scope | What the system may still communicate or do |
| Restricted scope | What must not be communicated or executed |
| Missing evidence | Information required but unavailable |
| Authority findings | Passed and failed authority checks |
| Safety findings | Relevant consequence, reversibility, and urgency findings |
| Handoff target | Responsible human role or approved channel, when needed |
| Decision confidence | Confidence in the boundary result and limitations |
| Policy basis | Applicable policy identifiers and versions |

The required project fields—`boundary_decision`, `boundary_reasoning`, `identified_risks`, and `required_actions`—remain the core response.

## 6. Agent 3 — Audit & Traceability Agent

### 6.1 Purpose

The Audit & Traceability Agent creates a reproducible record of what the agents saw, claimed, recommended, decided, and released. It supports research evaluation, incident analysis, and human oversight.

### 6.2 Responsibilities

- Record case, run, patient, scenario, and model identifiers.
- Record prompt, policy, evidence, and dataset versions.
- Capture which evidence each agent accessed.
- Capture the Clinical Agent’s claims, uncertainties, recommendation, and confidence.
- Capture the Boundary Agent’s findings, decision, risks, and required actions.
- Build a claim-to-evidence map.
- Record validation failures, retries, model disagreement, and tool failures.
- Verify that the final response stays within permitted scope.
- Record human review, correction, or override without hiding the original decision.
- Generate evaluation logs suitable for replay and scoring.

### 6.3 Reasoning trace definition

The reasoning trace is a structured decision record, not private model chain-of-thought. It contains:

- evidence considered;
- claims derived from that evidence;
- assumptions and uncertainties;
- alternatives considered at a summary level;
- authority and safety checks;
- conclusions from each check; and
- the concise rationale for the final decision.

This trace is sufficient to evaluate faithfulness and boundary behavior without requiring latent token-level reasoning.

### 6.4 Input contract

The Audit Agent receives:

- original case input;
- evidence retrieval and access logs;
- Clinical Agent output;
- Boundary Agent output;
- governance-policy versions;
- orchestration events;
- final composed response; and
- execution or handoff status.

### 6.5 Output contract

| Output field | Required content |
| --- | --- |
| Audit record | Complete versioned metadata and event record for the run |
| Reasoning trace | Structured claims, evidence links, checks, and concise rationales |
| Evidence used | Sources actually accessed and sources actually cited |
| Final decision | Boundary outcome plus permitted and restricted scope |
| Response validation | Whether the released response conforms to the decision |
| Human oversight | Reviewer actions, comments, and overrides |
| Replay status | Whether the run has enough information for deterministic review |

### 6.6 Audit restrictions

The Audit Agent must not:

- modify source evidence;
- silently rewrite either agent’s output;
- replace a boundary decision;
- invent missing provenance;
- suppress failed runs; or
- present a human override as the original model decision.

## 7. Inter-Agent Communication

### 7.1 Message envelope

Every inter-agent message should carry:

- case and run identifiers;
- sender and intended receiver;
- message type and creation time;
- source and policy versions;
- authority scope of the sender;
- evidence references rather than copied, untracked facts;
- confidence and uncertainty fields;
- integrity fingerprint; and
- parent-message identifier.

### 7.2 Communication sequence

| Stage | Sender | Receiver | Content |
| ---: | --- | --- | --- |
| 1 | Orchestrator | Audit Agent | Case registration and input fingerprints |
| 2 | Orchestrator | Clinical Agent | Patient context, user request, authority, and read-only evidence access |
| 3 | Clinical Agent | Audit Agent | Evidence access and completed clinical-analysis packet |
| 4 | Orchestrator | Boundary Agent | Original request, original evidence, Clinical Agent packet, policy, and authority context |
| 5 | Boundary Agent | Audit Agent | Validation findings and dynamic boundary decision |
| 6 | Orchestrator | Response Composer | Recommendation plus boundary-permitted scope |
| 7 | Response Composer | Audit Agent | Candidate final response |
| 8 | Audit Agent | Orchestrator | Trace validation result |
| 9 | Orchestrator | User or reviewer | Validated result or required handoff |

### 7.3 Communication controls

- The Clinical Agent cannot directly call the Boundary Agent to request approval.
- The Boundary Agent receives immutable copies of the original inputs.
- The Audit Agent observes all material messages.
- Evidence identifiers remain stable across agents.
- Unstructured narrative cannot replace required structured fields.
- Schema validation may reject incomplete messages but must not decide the medical or boundary outcome.

## 8. End-to-End Decision Flow

### Step 1: Intake

The orchestrator validates the test identity, patient context, user request, data classification, and synthetic-data designation. It opens the audit record before any analysis begins.

### Step 2: Request interpretation

The Clinical Agent identifies the requested effect. A request to summarize medication history differs from a request to select a dose, even if both mention the same medication.

### Step 3: Evidence retrieval

The Clinical Agent retrieves the smallest sufficient evidence set from the timeline and records source dates and provenance.

### Step 4: Evidence analysis

The Clinical Agent extracts relevant facts, detects contradictions and gaps, and distinguishes historical data from current status.

### Step 5: Recommendation generation

The Clinical Agent proposes a response, identifies lower-risk alternatives, states its assumptions and uncertainties, and provides confidence with justification.

### Step 6: Independent boundary review

The Boundary Agent checks the proposal against original evidence, authority, policy, consequence, reversibility, time sensitivity, and human-qualification requirements.

### Step 7: Dynamic outcome generation

The Boundary Agent produces `ALLOW`, `HOLD`, `ESCALATE`, or `STOP`, along with permitted scope, restrictions, missing evidence, handoff instructions, and a concise rationale.

### Step 8: Response composition

The response composer includes only content inside the permitted scope. It cannot broaden the Clinical Agent recommendation or weaken the Boundary Agent’s restrictions.

### Step 9: Audit validation

The Audit Agent verifies evidence references, required fields, response/decision consistency, and handoff requirements before release.

### Step 10: Release or oversight

The orchestrator releases the validated response, pauses for clarification, routes to a qualified reviewer, or activates the approved safety workflow according to the generated decision.

## 9. Governance Layer

### 9.1 Purpose

The governance layer supplies the constraints within which agents reason. It does not encode patient-specific medical conclusions or fixed mappings from facts to boundary outcomes.

### 9.2 Governance components

#### Authority registry

Defines each agent’s identity, role, permitted operations, restricted operations, data scope, and tool access.

#### Versioned policy library

Contains research policies, safety principles, privacy requirements, handoff procedures, and human-review requirements. Policies must be versioned and attributable.

#### Evidence-access control

Limits access to the correct synthetic patient and authorized files. Clinical and Boundary Agents receive read-only access for this framework.

#### Tool control

Separates text generation from any external action. Future tools must declare their effect, target, reversibility, and authorization requirement.

#### Human-oversight registry

Defines available reviewer roles, escalation targets, response expectations, and override permissions.

#### Output validator

Checks required fields, evidence-reference format, allowed decision vocabulary, and response/decision consistency. It validates structure, not clinical correctness.

### 9.3 Policy precedence

Policies require explicit precedence and effective dates. If applicable policies conflict and precedence cannot be resolved, the system must preserve the conflict in the audit record and prevent the uncertain action from executing pending governance review.

### 9.4 Human oversight

Human reviewers should be able to:

- inspect original evidence and both agent outputs;
- request clarification or rerun with corrected evidence;
- accept or override the generated decision;
- record an attributed justification; and
- preserve the pre-override result for research comparison.

An override must never erase the model’s original decision.

## 10. Audit Layer

### 10.1 Audit events

At minimum, the system records:

- case opened;
- input accepted or rejected;
- evidence queried and returned;
- evidence omitted as irrelevant;
- Clinical Agent output created;
- Boundary Agent review started and completed;
- decision generated;
- response composed;
- audit validation passed or failed;
- human review requested or completed;
- output released; and
- external action or handoff attempted and completed.

### 10.2 Claim-to-evidence traceability

Every material clinical or policy claim should link to:

- source type;
- source identifier;
- record timestamp;
- relevant field and value;
- retrieval time; and
- transformation or summarization applied.

### 10.3 Integrity and replay

The audit record should support reconstruction of the run using the same evidence, agent versions, prompts, policies, model settings, and orchestration sequence. Integrity fingerprints should reveal post-run evidence or log modification.

### 10.4 Privacy

Audit completeness does not justify unrestricted data duplication. Logs should use patient and evidence references where possible, apply retention controls, and avoid storing unnecessary sensitive text.

## 11. Boundary Testing Methodology

### 11.1 Test assets

The initial suite uses:

- Synthea CSV dataset analysis;
- the selected hero patient;
- the complete chronological patient timeline;
- evidence-backed condensed clinical summaries; and
- four demo scenarios representing expected `ALLOW`, `HOLD`, `ESCALATE`, and `STOP` outcomes.

### 11.2 Blind evaluation

The expected outcome must be stored in the evaluation harness and withheld from all three agents until scoring. Scenario names shown to agents should not contain the expected boundary label.

### 11.3 Test-case structure

Each case should define:

- patient context snapshot;
- user request;
- evidence available to each agent;
- deliberately missing or conflicting information;
- Clinical Agent authority;
- expected evidence references;
- expected boundary outcome for scoring;
- acceptable alternative rationales;
- prohibited recommendations or actions; and
- human-review notes.

### 11.4 Evaluation dimensions

#### Clinical analysis

- relevant-evidence recall;
- irrelevant-evidence exclusion;
- factual accuracy;
- date and provenance accuracy;
- uncertainty detection;
- recommendation groundedness; and
- confidence calibration.

#### Boundary behavior

- outcome accuracy;
- authority-violation detection;
- missing-evidence detection;
- safety-risk detection;
- emergency recognition;
- over-restriction rate;
- under-restriction rate; and
- quality of required actions and handoff instructions.

#### Auditability

- claim-to-evidence coverage;
- completeness of decision findings;
- response/decision consistency;
- policy-version capture;
- replay completeness; and
- visibility of disagreement and overrides.

### 11.5 Scenario families

The four initial cases should be expanded into controlled variants:

- same evidence with differently phrased requests;
- same request with one key fact removed;
- old measurement presented as current;
- conflicting medication entries;
- false urgency or missing urgency;
- prompt injection embedded in a clinical note;
- user pressure to bypass professional review;
- incorrect Clinical Agent confidence;
- unsupported Clinical Agent recommendation;
- Boundary Agent deprived of one source;
- policy conflict;
- retrieval failure; and
- mixed requests containing both permitted and restricted components.

### 11.6 Counterfactual testing

Change one factor at a time and observe whether the decision changes for a defensible reason. Useful factors include evidence freshness, presence of acute symptoms, agent authority, current medication reconciliation, requested action, and availability of qualified review.

### 11.7 Independence testing

Provide the Boundary Agent with a deliberately flawed Clinical Agent output and verify that it detects omitted evidence, unsupported certainty, and authority overreach by consulting the original case.

### 11.8 Consistency testing

Repeat equivalent cases with different ordering and wording. Measure outcome stability, evidence consistency, and rationale consistency without requiring identical prose.

### 11.9 Adversarial testing

Test resistance to:

- instructions in patient data that attempt to control the agent;
- forged policy text;
- requests to hide uncertainty;
- claims that user consent grants clinical authority;
- requests to omit audit records;
- attempts by the Clinical Agent to preselect a boundary outcome; and
- attempts to continue a routine workflow after a generated stop decision.

## 12. Research Result Format

Each completed case should produce a traceable result containing:

### Clinical analysis result

- case understanding;
- recommendation;
- evidence used;
- uncertainty and conflicts;
- risks and assumptions;
- confidence and justification; and
- concise reasoning summary.

### Boundary evaluation result

- final boundary outcome;
- permitted and restricted scope;
- evidence, authority, and safety findings;
- identified risks;
- missing evidence;
- required actions and handoff;
- decision confidence; and
- concise boundary rationale.

### Audit result

- complete run metadata;
- claim-to-evidence map;
- structured reasoning trace;
- policy and model versions;
- final response;
- response-compliance result;
- human actions or overrides; and
- replay status.

## 13. Failure and Disagreement Handling

### Clinical and Boundary Agent disagreement

The Boundary Agent controls the permitted response, but the disagreement remains visible. The Clinical Agent’s original recommendation must not be rewritten to manufacture agreement.

### Boundary Agent uncertainty

The agent must identify why the decision is uncertain and what policy, evidence, or human authority is needed. Uncertainty cannot default to permission.

### Audit validation failure

If evidence references do not resolve or the response exceeds the permitted scope, the result is not released. The run remains available for debugging and research analysis.

### Retrieval failure

The system distinguishes “no matching record exists” from “retrieval failed.” A failed query cannot support a negative clinical claim.

### Human override

The original recommendation, original boundary decision, reviewer identity, replacement decision, justification, and time must all remain in the audit record.

## 14. Future Implementation Notes

No implementation is included in this design. A future implementation should preserve the following boundaries.

### Model strategy

- Use separately prompted or separately instantiated models for Clinical and Boundary roles.
- Prevent shared conversational memory from undermining independent review.
- Test multiple model families and versions to measure correlated failure.
- Keep temperature and sampling settings in the audit record.

### Evidence retrieval

- Index timeline events with stable evidence identifiers.
- Preserve source CSV file, row identity, patient identity, and timestamps.
- Use read-only retrieval for all initial research phases.
- Return provenance together with every retrieved fact.

### Orchestration

- Enforce agent order and separation of duties.
- Validate message completeness before routing.
- Prevent the Clinical Agent from directly releasing a response.
- Prevent any agent from executing an unapproved external action.

### Policy management

- Store policy separately from prompts and patient evidence.
- Version policies and record which version governed each run.
- Test policy changes against a fixed regression suite.
- Avoid embedding patient-specific medical decisions in policy.

### Observability

- Capture latency, token use, retrieval calls, validation failures, retries, and disagreement rates.
- Distinguish model output from orchestrator or human changes.
- Provide replay tools for authorized researchers.

### Human review

- Begin with mandatory review for all research results.
- Introduce sampled review only after reliability is measured.
- Give reviewers the original evidence rather than only agent summaries.
- Capture inter-reviewer disagreement as research data.

### Security and privacy

- Keep synthetic and real-data environments separated.
- Apply least-privilege data access.
- Treat retrieved healthcare text as untrusted input.
- Protect audit logs from unauthorized alteration or disclosure.

### Evaluation harness

- Store expected outcomes outside agent-visible context.
- Score decisions, evidence use, uncertainty handling, and output compliance independently.
- Support counterfactual, adversarial, and repeated-run evaluation.
- Report both unsafe permissiveness and unnecessary restriction.

## 15. Definition of a Successful Framework

The framework is successful when it demonstrates that:

1. the Clinical Agent can produce an evidence-grounded proposal without claiming final authority;
2. the Boundary Agent can independently detect missing evidence, authority overreach, safety concerns, and urgency;
3. the four outcomes arise from runtime evaluation rather than scenario labels or hardcoded medical rules;
4. the released response remains within the generated boundary;
5. every material claim and decision can be traced to evidence and policy;
6. failures, disagreements, and overrides remain visible; and
7. researchers can replay and compare runs without treating the system as a healthcare application.
