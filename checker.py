import pysrt
import language_tool_python
import argparse
import sys

def check_grammar(text, tool):
    """Check grammar issues using LanguageTool."""
    matches = tool.check(text)
    return [m for m in matches if m.ruleId != "UPPERCASE_SENTENCE_START"]  # Example filter

def check_timing(subs):
    """Check for overlapping or improperly ordered captions."""
    issues = []
    for i in range(len(subs)-1):
        if subs[i].end > subs[i+1].start:
            issues.append(
                f"Overlap: Caption {subs[i].index} ends after Caption {subs[i+1].index} starts."
            )
    return issues

def main(file_path):
    tool = language_tool_python.LanguageTool('en-US')

    try:
        subs = pysrt.open(file_path)
    except Exception as e:
        print(f"Error reading subtitle file: {e}")
        sys.exit(1)

    # Check each caption
    for sub in subs:
        grammar_issues = check_grammar(sub.text, tool)
        for issue in grammar_issues:
            print(f"[GRAMMAR] Caption {sub.index}: {issue.message}")

    # Check timing issues
    timing_issues = check_timing(subs)
    for issue in timing_issues:
        print(f"[TIMING] {issue}")

    if not timing_issues and all(len(check_grammar(s.text, tool)) == 0 for s in subs):
        print("✅ All captions passed grammar and timing checks.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Video Caption Quality Checker")
    parser.add_argument("--file", required=True, help="Path to .srt subtitle file")
    args = parser.parse_args()
    main(args.file)
