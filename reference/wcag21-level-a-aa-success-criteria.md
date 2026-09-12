# WCAG 2.1 — Level A and Level AA Success Criteria (verbatim)

Source: W3C Recommendation, Web Content Accessibility Guidelines (WCAG) 2.1, https://www.w3.org/TR/WCAG21/ (the 21 September 2023 edition is the version at that URL). Fetched and extracted from the W3C HTML on 2026-09-11; the unmodified download is in `raw/wcag21.html`.
Copyright © 2017-2023 W3C® (MIT, ERCIM, Keio, Beihang). Reproduced under the W3C Document License. This file carries the normative text of every Level A and Level AA success criterion (the levels 28 CFR 35.200 requires). Level AAA criteria are omitted because no cited rule requires them.
Cite as: WCAG 2.1 SC <number> (<name>) (Level <A|AA>). Anchor: https://www.w3.org/TR/WCAG21/#<id>


---

## SC 1.1.1 Non-text Content (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#non-text-content

Success Criterion 1.1.1 Non-text Content

(Level A)

 All non-text content that is presented to the user has a text alternative that serves the equivalent purpose, except for the situations listed below.

 Controls, Input

 If non-text content is a control or accepts user input, then it has a name that describes its purpose. (Refer to Success Criterion 4.1.2 for additional requirements for controls and content that accepts user input.)

 Time-Based Media

 If non-text content is time-based media, then text alternatives at least provide descriptive
 identification of the non-text content. (Refer to Guideline 1.2 for additional requirements for media.)

 Test

 If non-text content is a test or exercise that would be invalid if presented in text, then text alternatives at least provide descriptive identification of the non-text
 content.

 Sensory

 If non-text content is primarily intended to create a specific sensory experience, then text alternatives at least provide descriptive identification of the non-text
 content.

 CAPTCHA

 If the purpose of non-text content is to confirm that content is being accessed by
 a person rather than a computer, then text alternatives that identify and describe
 the purpose of the non-text content are provided, and alternative forms of CAPTCHA
 using output modes for different types of sensory perception are provided to accommodate
 different disabilities.

 Decoration, Formatting, Invisible

 If non-text content is pure decoration, is used only for visual formatting, or is not presented to users, then it is implemented
 in a way that it can be ignored by assistive technology.

---

## SC 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#audio-only-and-video-only-prerecorded

Success Criterion 1.2.1 Audio-only and Video-only (Prerecorded)

(Level A)

 For prerecorded
 audio-only and prerecorded video-only media, the following are true, except when the audio or video is a media alternative for text and is clearly labeled as such:

 Prerecorded Audio-only

 An alternative for time-based media is provided that presents equivalent information for prerecorded audio-only content.

 Prerecorded Video-only

 Either an alternative for time-based media or an audio track is provided that presents
 equivalent information for prerecorded video-only content.

---

## SC 1.2.2 Captions (Prerecorded) (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#captions-prerecorded

Success Criterion 1.2.2 Captions (Prerecorded)

(Level A)

 Captions are provided for all prerecorded
 audio content in synchronized media, except when the media is a media alternative for text and is clearly labeled as such.

---

## SC 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#audio-description-or-media-alternative-prerecorded

Success Criterion 1.2.3 Audio Description or Media Alternative (Prerecorded)

(Level A)

 An alternative for time-based media or audio description of the prerecorded
 video content is provided for synchronized media, except when the media is a media alternative for text and is clearly labeled as such.

---

## SC 1.2.4 Captions (Live) (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#captions-live

Success Criterion 1.2.4 Captions (Live)

(Level AA)

 Captions are provided for all live
 audio content in synchronized media.

---

## SC 1.2.5 Audio Description (Prerecorded) (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#audio-description-prerecorded

Success Criterion 1.2.5 Audio Description (Prerecorded)

(Level AA)

 Audio description is provided for all prerecorded
 video content in synchronized media.

---

## SC 1.3.1 Info and Relationships (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#info-and-relationships

Success Criterion 1.3.1 Info and Relationships

(Level A)

 Information, structure, and relationships conveyed through presentation can be programmatically determined or are available in text.

---

## SC 1.3.2 Meaningful Sequence (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#meaningful-sequence

Success Criterion 1.3.2 Meaningful Sequence

(Level A)

 When the sequence in which content is presented affects its meaning, a correct reading sequence can be programmatically determined.

---

## SC 1.3.3 Sensory Characteristics (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#sensory-characteristics

Success Criterion 1.3.3 Sensory Characteristics

(Level A)

 Instructions provided for understanding and operating content do not rely solely on
 sensory characteristics of components such as shape, color, size, visual location, orientation,
 or sound.

 Note
For requirements related to color, refer to Guideline 1.4.

---

## SC 1.3.4 Orientation (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#orientation

Success Criterion 1.3.4 Orientation

(Level AA)

 Content does not restrict its view and operation to a single display orientation, such as portrait or landscape, unless a specific display orientation is essential.

 Note
Examples where a particular display orientation may be essential are a bank check, a piano application, slides for a projector or television, or virtual reality content where content is not necessarily restricted to landscape or portrait display orientation.

---

## SC 1.3.5 Identify Input Purpose (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#identify-input-purpose

Success Criterion 1.3.5 Identify Input Purpose

(Level AA)

 The purpose of each input field collecting information about the user can be programmatically determined when:

 - The input field serves a purpose identified in the Input Purposes for user interface components section; and

 - The content is implemented using technologies with support for identifying the expected meaning for form input data.

---

## SC 1.4.1 Use of Color (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#use-of-color

Success Criterion 1.4.1 Use of Color

(Level A)

 Color is not used as the only visual means of conveying information, indicating an
 action, prompting a response, or distinguishing a visual element.

 Note
This success criterion addresses color perception specifically. Other forms of perception are covered in Guideline 1.3 including programmatic access to color and other visual presentation coding.

---

## SC 1.4.2 Audio Control (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#audio-control

Success Criterion 1.4.2 Audio Control

(Level A)

 If any audio on a web page plays automatically for more than 3 seconds, either a mechanism is available to pause or stop the audio, or a mechanism is available to control audio
 volume independently from the overall system volume level.

 Note
Since any content that does not meet this success criterion can interfere with a user's
 ability to use the whole page, all content on the web page (whether or not it is used
 to meet other success criteria) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

---

## SC 1.4.3 Contrast (Minimum) (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#contrast-minimum

Success Criterion 1.4.3 Contrast (Minimum)

(Level AA)

 The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for the following:

 Large Text

 Large-scale text and images of large-scale text have a contrast ratio of at least 3:1;

 Incidental

 Text or images of text that are part of an inactive user interface component, that are pure decoration, that are not visible to anyone, or that are part of a picture that contains significant
 other visual content, have no contrast requirement.

 Logotypes

 Text that is part of a logo or brand name has no contrast requirement.

---

## SC 1.4.4 Resize Text (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#resize-text

Success Criterion 1.4.4 Resize Text

(Level AA)

 Except for captions and images of text, text can be resized without assistive technology up to 200 percent without loss of content or functionality.

---

## SC 1.4.5 Images of Text (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#images-of-text

Success Criterion 1.4.5 Images of Text

(Level AA)

 If the technologies being used can achieve the visual presentation, text is used to convey information rather than images of text except for the following:

 Customizable

 The image of text can be visually customized to the user's requirements;

 Essential

 A particular presentation of text is essential to the information being conveyed.

 Note
Logotypes (text that is part of a logo or brand name) are considered essential.

---

## SC 1.4.10 Reflow (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#reflow

Success Criterion 1.4.10 Reflow

(Level AA)

 Content can be presented without loss of information or functionality, and without requiring scrolling in two dimensions for:

 - Vertical scrolling content at a width equivalent to 320 CSS pixels;

 - Horizontal scrolling content at a height equivalent to 256 CSS pixels.

 Except for parts of the content which require two-dimensional layout for usage or meaning.

 Note 1
320 CSS pixels is equivalent to a starting viewport width of 1280 CSS pixels wide at 400% zoom. For web content which is designed to scroll horizontally (e.g., with vertical text), 256 CSS pixels is equivalent to a starting viewport height of 1024 CSS pixels at 400% zoom.

 Note 2
Examples of content which requires two-dimensional layout are images required for understanding (such as maps and diagrams), video, games, presentations, data tables (not individual cells), and interfaces where it is necessary to keep toolbars in view while manipulating content. It is acceptable to provide two-dimensional scrolling for such parts of the content.

---

## SC 1.4.11 Non-text Contrast (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#non-text-contrast

Success Criterion 1.4.11 Non-text Contrast

(Level AA)

 The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s):

 User Interface Components

 Visual information required to identify user interface components and states, except for inactive components or where the appearance of the component is determined by the user agent and not modified by the author;

 Graphical Objects

 Parts of graphics required to understand the content, except when a particular presentation of graphics is essential to the information being conveyed.

---

## SC 1.4.12 Text Spacing (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#text-spacing

Success Criterion 1.4.12 Text Spacing

(Level AA)

 In content implemented using markup languages that support the following text style properties, no loss of content or functionality occurs by setting all of the following and by changing no other style property:

 - Line height (line spacing) to at least 1.5 times the font size;

 - Spacing following paragraphs to at least 2 times the font size;

 - Letter spacing (tracking) to at least 0.12 times the font size;

 - Word spacing to at least 0.16 times the font size.

 Exception: Human languages and scripts that do not make use of one or more of these text style properties in written text can conform using only the properties that exist for that combination of language and script.

---

## SC 1.4.13 Content on Hover or Focus (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#content-on-hover-or-focus

Success Criterion 1.4.13 Content on Hover or Focus

(Level AA)

 Where receiving and then removing pointer hover or keyboard focus triggers additional content to become visible and then hidden, the following are true:

 Dismissible

 A mechanism is available to dismiss the additional content without moving pointer hover or keyboard focus, unless the additional content communicates an input error or does not obscure or replace other content;

 Hoverable

 If pointer hover can trigger the additional content, then the pointer can be moved over the additional content without the additional content disappearing;

 Persistent

 The additional content remains visible until the hover or focus trigger is removed, the user dismisses it, or its information is no longer valid.

 Exception: The visual presentation of the additional content is controlled by the user agent and is not modified by the author.

 Note 1
Examples of additional content controlled by the user agent include browser tooltips created through use of the HTML title attribute.

 Note 2
Custom tooltips, sub-menus, and other nonmodal popups that display on hover and focus are examples of additional content covered by this criterion.

---

## SC 2.1.1 Keyboard (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#keyboard

Success Criterion 2.1.1 Keyboard

(Level A)

 All functionality of the content is operable through a keyboard interface without requiring specific timings for individual keystrokes, except where the underlying
 function requires input that depends on the path of the user's movement and not just
 the endpoints.

 Note 1
This exception relates to the underlying function, not the input technique. For example,
 if using handwriting to enter text, the input technique (handwriting) requires path-dependent
 input but the underlying function (text input) does not.

 Note 2
This does not forbid and should not discourage providing mouse input or other input
 methods in addition to keyboard operation.

---

## SC 2.1.2 No Keyboard Trap (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#no-keyboard-trap

Success Criterion 2.1.2 No Keyboard Trap

(Level A)

 If keyboard focus can be moved to a component of the page using a keyboard interface, then focus can be moved away from that component using only a keyboard interface,
 and, if it requires more than unmodified arrow or tab keys or other standard exit
 methods, the user is advised of the method for moving focus away.

 Note
Since any content that does not meet this success criterion can interfere with a user's
 ability to use the whole page, all content on the web page (whether it is used to
 meet other success criteria or not) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

---

## SC 2.1.4 Character Key Shortcuts (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#character-key-shortcuts

Success Criterion 2.1.4 Character Key Shortcuts

(Level A)

 If a keyboard shortcut is implemented in content using only letter (including upper- and lower-case letters), punctuation, number, or symbol characters, then at least one of the following is true:

 Turn off

 A mechanism is available to turn the shortcut off;

 Remap

 A mechanism is available to remap the shortcut to include one or more non-printable keyboard keys (e.g., Ctrl, Alt);

 Active only on focus

 The keyboard shortcut for a user interface component is only active when that component has focus.

---

## SC 2.2.1 Timing Adjustable (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#timing-adjustable

Success Criterion 2.2.1 Timing Adjustable

(Level A)

 For each time limit that is set by the content, at least one of the following is true:

 Turn off

 The user is allowed to turn off the time limit before encountering it; or

 Adjust

 The user is allowed to adjust the time limit before encountering it over a wide range
 that is at least ten times the length of the default setting; or

 Extend

 The user is warned before time expires and given at least 20 seconds to extend the
 time limit with a simple action (for example, "press the space bar"), and the user
 is allowed to extend the time limit at least ten times; or

 Real-time Exception

 The time limit is a required part of a real-time event (for example, an auction),
 and no alternative to the time limit is possible; or

 Essential Exception

 The time limit is essential and extending it would invalidate the activity; or

 20 Hour Exception

 The time limit is longer than 20 hours.

 Note
This success criterion helps ensure that users can complete tasks without unexpected
 changes in content or context that are a result of a time limit. This success criterion
 should be considered in conjunction with Success Criterion 3.2.1, which puts limits on changes of content or context as a result of user action.

---

## SC 2.2.2 Pause, Stop, Hide (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#pause-stop-hide

Success Criterion 2.2.2 Pause, Stop, Hide

(Level A)

 For moving, blinking, scrolling, or auto-updating information, all of the following are true:

 Moving, blinking, scrolling

 For any moving, blinking or scrolling information that (1) starts automatically, (2)
 lasts more than five seconds, and (3) is presented in parallel with other content,
 there is a mechanism for the user to pause, stop, or hide it unless the movement, blinking, or scrolling is part of an activity
 where it is essential; and

 Auto-updating

 For any auto-updating information that (1) starts automatically and (2) is presented
 in parallel with other content, there is a mechanism for the user to pause, stop,
 or hide it or to control the frequency of the update unless the auto-updating is part
 of an activity where it is essential.

 Note 1
For requirements related to flickering or flashing content, refer to Guideline 2.3.

 Note 2
Since any content that does not meet this success criterion can interfere with a user's
 ability to use the whole page, all content on the web page (whether it is used to
 meet other success criteria or not) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

 Note 3
Content that is updated periodically by software or that is streamed to the user agent
 is not required to preserve or present information that is generated or received between
 the initiation of the pause and resuming presentation, as this may not be technically
 possible, and in many situations could be misleading to do so.

 Note 4
An animation that occurs as part of a preload phase or similar situation can be considered
 essential if interaction cannot occur during that phase for all users and if not indicating
 progress could confuse users or cause them to think that content was frozen or broken.

---

## SC 2.3.1 Three Flashes or Below Threshold (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#three-flashes-or-below-threshold

Success Criterion 2.3.1 Three Flashes or Below Threshold

(Level A)

 Web pages do not contain anything that flashes more than three times in any one second period,
 or the flash is below the general flash and red flash thresholds.

 Note
Since any content that does not meet this success criterion can interfere with a user's
 ability to use the whole page, all content on the web page (whether it is used to
 meet other success criteria or not) must meet this success criterion. See Conformance Requirement 5: Non-Interference.

---

## SC 2.4.1 Bypass Blocks (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#bypass-blocks

Success Criterion 2.4.1 Bypass Blocks

(Level A)

 A mechanism is available to bypass blocks of content that are repeated on multiple web pages.

---

## SC 2.4.2 Page Titled (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#page-titled

Success Criterion 2.4.2 Page Titled

(Level A)

 Web pages have titles that describe topic or purpose.

---

## SC 2.4.3 Focus Order (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#focus-order

Success Criterion 2.4.3 Focus Order

(Level A)

 If a web page can be navigated sequentially and the navigation sequences affect meaning or operation, focusable components receive
 focus in an order that preserves meaning and operability.

---

## SC 2.4.4 Link Purpose (In Context) (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#link-purpose-in-context

Success Criterion 2.4.4 Link Purpose (In Context)

(Level A)

 The purpose of each link can be determined from the link text alone or from the link text together with its
 programmatically determined link context, except where the purpose of the link would be ambiguous to users in general.

---

## SC 2.4.5 Multiple Ways (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#multiple-ways

Success Criterion 2.4.5 Multiple Ways

(Level AA)

 More than one way is available to locate a web page within a set of web pages except where the web page is the result of, or a step in, a process.

---

## SC 2.4.6 Headings and Labels (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#headings-and-labels

Success Criterion 2.4.6 Headings and Labels

(Level AA)

 Headings and labels describe topic or purpose.

---

## SC 2.4.7 Focus Visible (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#focus-visible

Success Criterion 2.4.7 Focus Visible

(Level AA)

 Any keyboard operable user interface has a mode of operation where the keyboard focus indicator is visible.

---

## SC 2.5.1 Pointer Gestures (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#pointer-gestures

Success Criterion 2.5.1 Pointer Gestures

(Level A)

 All functionality that uses multipoint or path-based gestures for operation can be operated with a single pointer without a path-based gesture, unless a multipoint or path-based gesture is essential.

 Note
This requirement applies to web content that interprets pointer actions (i.e. this does not apply to actions that are required to operate the user agent or assistive technology).

---

## SC 2.5.2 Pointer Cancellation (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#pointer-cancellation

Success Criterion 2.5.2 Pointer Cancellation

(Level A)

 For functionality that can be operated using a single pointer, at least one of the following is true:

 No Down-Event

 The down-event of the pointer is not used to execute any part of the function;

 Abort or Undo

 Completion of the function is on the up-event, and a mechanism is available to abort the function before completion or to undo the function after completion;

 Up Reversal

 The up-event reverses any outcome of the preceding down-event;

 Essential

 Completing the function on the down-event is essential.

 Note 1
Functions that emulate a keyboard or numeric keypad key press are considered essential.

 Note 2
This requirement applies to web content that interprets pointer actions (i.e. this does not apply to actions that are required to operate the user agent or assistive technology).

---

## SC 2.5.3 Label in Name (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#label-in-name

Success Criterion 2.5.3 Label in Name

(Level A)

 For user interface components with labels that include text or images of text, the name contains the text that is presented visually.

 Note
A best practice is to have the text of the label at the start of the name.

---

## SC 2.5.4 Motion Actuation (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#motion-actuation

Success Criterion 2.5.4 Motion Actuation

(Level A)

 Functionality that can be operated by device motion or user motion can also be operated by user interface components and responding to the motion can be disabled to prevent accidental actuation, except when:

 Supported Interface

 The motion is used to operate functionality through an accessibility supported interface;

 Essential

 The motion is essential for the function and doing so would invalidate the activity.

---

## SC 3.1.1 Language of Page (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#language-of-page

Success Criterion 3.1.1 Language of Page

(Level A)

 The default human language of each web page can be programmatically determined.

---

## SC 3.1.2 Language of Parts (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#language-of-parts

Success Criterion 3.1.2 Language of Parts

(Level AA)

 The human language of each passage or phrase in the content can be programmatically determined except for proper names, technical terms, words of indeterminate language, and words
 or phrases that have become part of the vernacular of the immediately surrounding
 text.

---

## SC 3.2.1 On Focus (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#on-focus

Success Criterion 3.2.1 On Focus

(Level A)

 When any user interface component receives focus, it does not initiate a change of context.

---

## SC 3.2.2 On Input (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#on-input

Success Criterion 3.2.2 On Input

(Level A)

 Changing the setting of any user interface component does not automatically cause a change of context unless the user has been advised of the behavior before using the component.

---

## SC 3.2.3 Consistent Navigation (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#consistent-navigation

Success Criterion 3.2.3 Consistent Navigation

(Level AA)

 Navigational mechanisms that are repeated on multiple web pages within a set of web pages occur in the same relative order each time they are repeated, unless a change is initiated by the user.

---

## SC 3.2.4 Consistent Identification (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#consistent-identification

Success Criterion 3.2.4 Consistent Identification

(Level AA)

 Components that have the same functionality within a set of web pages are identified consistently.

---

## SC 3.3.1 Error Identification (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#error-identification

Success Criterion 3.3.1 Error Identification

(Level A)

 If an input error is automatically detected, the item that is in error is identified and the error
 is described to the user in text.

---

## SC 3.3.2 Labels or Instructions (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#labels-or-instructions

Success Criterion 3.3.2 Labels or Instructions

(Level A)

 Labels or instructions are provided when content requires user input.

---

## SC 3.3.3 Error Suggestion (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#error-suggestion

Success Criterion 3.3.3 Error Suggestion

(Level AA)

 If an input error is automatically detected and suggestions for correction are known, then the suggestions
 are provided to the user, unless it would jeopardize the security or purpose of the
 content.

---

## SC 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#error-prevention-legal-financial-data

Success Criterion 3.3.4 Error Prevention (Legal, Financial, Data)

(Level AA)

 For web pages that cause legal commitments or financial transactions for the user to occur, that modify or delete user-controllable data in data storage systems, or that submit user test responses, at least one of
 the following is true:

 Reversible
Submissions are reversible.

 Checked
Data entered by the user is checked for input errors and the user is provided an opportunity to correct them.

 Confirmed
A mechanism is available for reviewing, confirming, and correcting information before finalizing the submission.

---

## SC 4.1.1 Parsing (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#parsing

Success Criterion 4.1.1 Parsing

(Level A)

 In content implemented using markup languages, elements have complete start and end
 tags, elements are nested according to their specifications, elements do not contain
 duplicate attributes, and any IDs are unique, except where the specifications allow
 these features.

 Note 1
This success criterion should be considered as always satisfied for any content using HTML or XML.

 Note 2

 Since this criterion was written, the HTML Living Standard has adopted specific requirements governing how user agents must handle incomplete tags, incorrect element nesting, duplicate attributes, and non-unique IDs. [HTML]

 Although the HTML standard treats some of these cases as non-conforming for authors, it is considered to "allow these features" for the purposes of this success criterion because the specification requires that user agents support handling these cases consistently. In practice, this criterion no longer provides any benefit to people with disabilities in itself.

 Issues such as missing roles due to inappropriately nested elements or incorrect states or names due to a duplicate ID are covered by different success criteria and should be reported under those criteria rather than as issues with 4.1.1.

---

## SC 4.1.2 Name, Role, Value (Level A)

Anchor: https://www.w3.org/TR/WCAG21/#name-role-value

Success Criterion 4.1.2 Name, Role, Value

(Level A)

 For all user interface components (including but not limited to: form elements, links and components generated by scripts),
 the name and role can be programmatically determined; states, properties, and values that can be set by the user can be programmatically set; and notification of changes to these items is available to user agents, including assistive technologies.

 Note
This success criterion is primarily for web authors who develop or script their own
 user interface components. For example, standard HTML controls already meet this success
 criterion when used according to specification.

---

## SC 4.1.3 Status Messages (Level AA)

Anchor: https://www.w3.org/TR/WCAG21/#status-messages

Success Criterion 4.1.3 Status Messages

(Level AA)

 In content implemented using markup languages, status messages can be programmatically determined through role or properties such that they can be presented to the user by assistive technologies without receiving focus.
