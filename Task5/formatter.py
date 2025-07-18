def format_resume(data, format="txt"):
    lines = []

    lines.append(f"# {data['name']}" if format == "md" else data["name"])
    lines.append(f"📧 {data['email']} | 📞 {data['phone']}")
    lines.append("")

    lines.append("## Summary" if format == "md" else "Summary:")
    lines.append(data["summary"])
    lines.append("")

    lines.append("## Skills" if format == "md" else "Skills:")
    lines.append(", ".join(data["skills"]))
    lines.append("")

    lines.append("## Experience" if format == "md" else "Experience:")
    for job in data["experience"]:
        lines.append(
            f"- {job['role']} at {job['company']} ({job['duration']})")

    lines.append("")
    lines.append("## Education" if format == "md" else "Education:")
    for edu in data["education"]:
        lines.append(f"- {edu['degree']}, {edu['school']} ({edu['year']})")

    return "\n".join(lines)
