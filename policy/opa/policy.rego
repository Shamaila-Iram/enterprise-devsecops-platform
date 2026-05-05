package kubernetes.admission

deny[msg] {
  input.kind == "Pod"
  input.spec.containers[_].securityContext.privileged == true
  msg := "Privileged containers are not allowed"
}