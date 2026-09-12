# WCAG 2.1 — definitions: contrast ratio, relative luminance, large scale (verbatim)

Source: W3C Recommendation WCAG 2.1, section 5 Glossary, https://www.w3.org/TR/WCAG21/#glossary . Extracted from `raw/wcag21.html`, fetched 2026-09-11. These are the definitions SC 1.4.3 depends on; `tools/audit.py` and rules.md §5 implement exactly this formula.

## contrast ratio

(L1 + 0.05) / (L2 + 0.05), where

 - L1 is the relative luminance of the lighter of the colors, and

 - L2 is the relative luminance of the darker of the colors.

 Note 1
Contrast ratios can range from 1 to 21 (commonly written 1:1 to 21:1).

 Note 2
Because authors do not have control over user settings as to how text is rendered
 (for example font smoothing or anti-aliasing), the contrast ratio for text can be
 evaluated with anti-aliasing turned off.

 Note 3
For the purpose of Success Criteria 1.4.3 and 1.4.6, contrast is measured with respect
 to the specified background over which the text is rendered in normal usage. If no
 background color is specified, then white is assumed.

 Note 4
Background color is the specified color of content over which the text is to be rendered
 in normal usage. It is a failure if no background color is specified when the text
 color is specified, because the user's default background color is unknown and cannot
 be evaluated for sufficient contrast. For the same reason, it is a failure if no text
 color is specified when a background color is specified.

 Note 5
When there is a border around the letter, the border can add contrast and would be
 used in calculating the contrast between the letter and its background. A narrow border
 around the letter would be used as the letter. A wide border around the letter that
 fills in the inner details of the letters acts as a halo and would be considered background.

 Note 6
WCAG conformance should be evaluated for color pairs specified in the content that
 an author would expect to appear adjacent in typical presentation. Authors need not
 consider unusual presentations, such as color changes made by the user agent, except
 where caused by authors' code.

## relative luminance

the relative brightness of any point in a colorspace, normalized to 0 for darkest
 black and 1 for lightest white

 Note 1

 For the sRGB colorspace, the relative luminance of a color is defined as L = 0.2126
 * R + 0.7152 * G + 0.0722 * B where R, G and B are defined as:

 - if RsRGB <= 0.04045 then R = RsRGB/12.92 else R = ((RsRGB+0.055)/1.055) ^ 2.4

 - if GsRGB <= 0.04045 then G = GsRGB/12.92 else G = ((GsRGB+0.055)/1.055) ^ 2.4

 - if BsRGB <= 0.04045 then B = BsRGB/12.92 else B = ((BsRGB+0.055)/1.055) ^ 2.4

 and RsRGB, GsRGB, and BsRGB are defined as:

 - RsRGB = R8bit/255

 - GsRGB = G8bit/255

 - BsRGB = B8bit/255

 The "^" character is the exponentiation operator. (Formula taken from 
 [SRGB].)

 Note 2
Before May 2021 the value of 0.04045 in the definition was different (0.03928). It was taken from an older version of the specification and has been updated. It has no practical effect on the calculations in the context of these guidelines.

 Note 3
Almost all systems used today to view web content assume sRGB encoding. Unless it
 is known that another color space will be used to process and display the content,
 authors should evaluate using sRGB colorspace. If using other color spaces, see Understanding Success Criterion 1.4.3.

 Note 4
If dithering occurs after delivery, then the source color value is used. For colors
 that are dithered at the source, the average values of the colors that are dithered
 should be used (average R, average G, and average B).

 Note 5
Tools are available that automatically do the calculations when testing contrast and
 flash.

 Note 6
A separate page giving the relative luminance definition using MathML to display the formulas is available.

## large scale (text)

with at least 18 point or 14 point bold or font size that would yield equivalent size
 for Chinese, Japanese and Korean (CJK) fonts

 Note 1
Fonts with extraordinarily thin strokes or unusual features and characteristics that
 reduce the familiarity of their letter forms are harder to read, especially at lower
 contrast levels.

 Note 2
Font size is the size when the content is delivered. It does not include resizing
 that may be done by a user.

 Note 3
The actual size of the character that a user sees is dependent both on the author-defined
 size and the user's display or user agent settings. For many mainstream body text
 fonts, 14 and 18 point is roughly equivalent to 1.2 and 1.5 em or to 120% or 150%
 of the default size for body text (assuming that the body font is 100%), but authors
 would need to check this for the particular fonts in use. When fonts are defined in
 relative units, the actual point size is calculated by the user agent for display.
 The point size should be obtained from the user agent, or calculated based on font
 metrics as the user agent does, when evaluating this success criterion. Users who
 have low vision would be responsible for choosing appropriate settings.

 Note 4
When using text without specifying the font size, the smallest font size used on major
 browsers for unspecified text would be a reasonable size to assume for the font. If
 a level 1 heading is rendered in 14pt bold or higher on major browsers, then it would
 be reasonable to assume it is large text. Relative scaling can be calculated from
 the default sizes in a similar fashion.

 Note 5
The 18 and 14 point sizes for roman texts are taken from the minimum size for large
 print (14pt) and the larger standard font size (18pt). For other fonts such as CJK
 languages, the "equivalent" sizes would be the minimum large print size used for those
 languages and the next larger standard large print size.
